from typing import List

from app.entities.covid_case import CaseObservation
from app.services.data_provider import CovidDataProvider
from app.utils import get_values_of_dict, read_csv_file


class CsvCovidDataProvider(CovidDataProvider):

    def __init__(self, file_path):
        self.file_path = file_path

    def get_data(self) -> List[CaseObservation]:

        lines = read_csv_file(self.file_path)

        if len(lines) == 0:
            return []

        cases = []
        for line in lines:
            cases.append(CaseObservation.get_csv_row_to_dict(line))

        # group cases based on a country and date
        groups = self.group_cases_by_country_and_date(cases)

        items: List[CaseObservation] = get_values_of_dict(groups)
        items = sorted(items, key=lambda case: case.country.country_name.lower().strip())

        return items
