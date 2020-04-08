from app.entities.option import ConsoleOption
from app.services.dispatching import BaseConsoleDispatcher
from app.utils import PrettyPrint


class AnalysisService(BaseConsoleDispatcher):
    """
    Service class to hold all business logic related to covid-19 cases.
    """

    def __init__(self):
        self.file_contents = None
        self.cases = None

    def __setup__(self):
        pass

    def show_all_cases(self):
        """
        Function that prints all the cases happened in world due to corona-virus
        (grouped by country) each date ordered by country name.
        :return: nothing
        """
        # TODO : implement me
        self.cases = None
        PrettyPrint.warn('not implemented')

    def show_all_cases_with_pagination(self, page_number=1):
        """
        Function that prints all the cases happened in world due to corona-virus
        (grouped by country) each date ordered by country name. (paginated)
        :return: nothing
        """
        # TODO : implement me
        self.cases = None
        PrettyPrint.warn('not implemented')

    def show_country_stats(self, country_name):
        """
        Function that prints stats related to a country.(grouped by country) .
        such as : total cases, total deaths, total recovered and observation date of first case
        :return: nothing
        """
        # TODO : implement me
        self.cases = None
        PrettyPrint.warn('not implemented')

    def show_peak_case_for_country(self, country_name):
        """
        Function that prints max no of cases occured in a particular function.
        :return: nothing
        """
        # TODO : implement me
        self.cases = None
        PrettyPrint.warn('not implemented')

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
