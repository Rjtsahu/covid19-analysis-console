from copy import deepcopy
from datetime import datetime
from typing import List, Tuple

from app.entities.constants import CSV_FILE_PATH, PAGE_SIZE
from app.entities.covid_case import CaseObservation
from app.entities.option import ConsoleOption
from app.exceptions.console_exceptions import InvalidInputException
from app.services.csv_data_provider import CsvCovidDataProvider
from app.services.data_provider import CovidDataProvider
from app.services.dispatching import BaseConsoleDispatcher
from app.utils import PrettyPrint


class AnalysisService(BaseConsoleDispatcher):
    """
    Service class to hold all business logic related to covid-19 cases.
    """
    table_headings = ['Date', 'Country', 'Cases', 'Deaths', 'Recovered']
    visible_record_count = 50

    def __init__(self, provider: CovidDataProvider = None):
        self.provider = provider or CsvCovidDataProvider(CSV_FILE_PATH)
        self.cases: List[CaseObservation] = self.provider.get_data()

    def show_all_cases(self):
        """
        Function that prints all the cases happened in world due to corona-virus
        (grouped by country) each date ordered by country name.
        :return: nothing
        """
        cases_to_show = deepcopy(self.cases)

        start_index = 0
        end_index = self.visible_record_count

        try:
            while (start_index == 0 or input() != 'q') and len(cases_to_show) > start_index:
                self.print_cases(cases_to_show[start_index:end_index])

                PrettyPrint.success(
                    'Showing record for %s to %s of %s ' % (start_index + 1, end_index, len(cases_to_show)))
                PrettyPrint.success('Press any key to continue | Type "q" and press enter to quit')

                start_index += self.visible_record_count
                end_index += self.visible_record_count

        except KeyboardInterrupt:
            PrettyPrint.info(' Navigating to Main menu.')

    def show_all_cases_with_pagination(self, page_number=1):
        """
        Function that prints all the cases happened in world due to corona-virus
        (grouped by country) each date ordered by country name. (paginated)
        :return: nothing
        """
        if not isinstance(page_number, int):
            if str(page_number).isdigit():
                page_number = int(page_number)
            else:
                raise InvalidInputException('Invalid page number : %s' % (page_number,))
        if page_number < 1:
            page_number = 1

        cases_to_show = deepcopy(self.cases)

        start_index = PAGE_SIZE * (page_number - 1)
        end_index = start_index + PAGE_SIZE

        if start_index >= len(cases_to_show):
            PrettyPrint.error('Page doesnt exists.')
        else:
            self.print_cases(cases_to_show[start_index:end_index])

    def show_country_stats(self, country_name):
        """
        Function that prints stats related to a country.(grouped by country) .
        such as : total cases, total deaths, total recovered and observation date of first case
        :return: nothing
        """
        country_cases = self.__get_cases_for_country__(country_name)
        if not country_cases:
            raise InvalidInputException('Invalid country name %s' % (country_name,))
        # get record having max cases.
        record = max(country_cases, key=lambda case: case.observation.confirmed)

        PrettyPrint.success(record)

    def show_peak_case_for_country(self, country_name):
        """
        Function that prints max no of cases occurred in a particular date.
        :return: nothing
        """
        record, peek_cases = self.__get_peak_case_for_country__(country_name)

        PrettyPrint.info("Peak cases: %s" % (peek_cases,))
        PrettyPrint.success(record)

    def get_options(self):
        return [
            ConsoleOption(
                title='Show all cases',
                description='Operation to print table that shows all the covid-19 cases occurred '
                            'in world ordered and grouped by country name.',
                invoke_key=0,
                action=self.show_all_cases),

            ConsoleOption(
                title='Show paginated cases bases on input page number',
                description='Operation to print table that shows all the covid-19 cases occurred '
                            'in world ordered and grouped by country name with pagination, need '
                            'extra argument that is page number which is optional and default value is 1.',
                invoke_key=1,
                action=self.show_all_cases_with_pagination),

            ConsoleOption(
                title='Show stats for a country.',
                description='Operation to print stats for a country '
                            'such as total cases, total deaths, total recovered and observation date of first case.'
                            'Need input argument that is country name.',
                invoke_key=2,
                action=self.show_country_stats),

            ConsoleOption(
                title='Show date of peek no of cases.',
                description='Operation to print date and cases when peak no of cases occurred in a particular country.'
                            'Need input argument that is country name.',
                invoke_key=3,
                action=self.show_peak_case_for_country)
        ]

    @classmethod
    def print_cases(cls, cases: List[CaseObservation]):
        cases_data = [[case.observation_date, case.country.country_name, case.observation.confirmed,
                       case.observation.deaths, case.observation.recovered] for case in cases]

        PrettyPrint.tabular(cls.table_headings, cases_data)

    def __get_cases_for_country__(self, country_name) -> List[CaseObservation]:
        """
        Function filters cases based on country name (case insensitive)
        :param country_name: name of country
        :return: list of case_observation
        """
        country_cases = []

        for item in self.cases:
            if item.country.country_name.lower() == country_name.lower():
                country_cases.append(deepcopy(item))

        return country_cases

    def __get_peak_case_for_country__(self, country_name) -> Tuple[CaseObservation, int]:
        """
        Function to find case having max diff (peak) of case from one-dey to another (asc order of date)
        :param country_name: country_name
        :return: tuple of case and peek case count
        """

        country_cases = self.__get_cases_for_country__(country_name)
        if not country_cases:
            raise InvalidInputException('Invalid country name %s' % (country_name,))

        # sort record with date (observation_date)
        country_cases = sorted(country_cases, key=lambda _case: datetime.strptime(_case.observation_date, '%m/%d/%Y'))

        max_diff = 0
        case = country_cases[0]

        for index in range(len(country_cases) - 1):
            diff = country_cases[index + 1].observation.confirmed - country_cases[index].observation.confirmed
            if diff >= max_diff:
                max_diff = diff
                case = country_cases[index + 1]

        return case, max_diff
