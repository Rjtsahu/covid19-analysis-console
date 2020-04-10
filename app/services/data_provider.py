from typing import List, Dict

from app.entities.country import Country
from app.entities.covid_case import CaseObservation, Observation


class CovidDataProvider(object):

    def get_data(self) -> List[CaseObservation]:
        """Abstract base class to fetch list of covid cases."""
        raise Exception("Need to extend this method")

    @classmethod
    def group_cases_by_country_and_date(cls, cases: List[Dict[str, str]]):
        # lets create a map of date-country : CovidObservation
        groups = {}
        for case in cases:
            key = "{date}-{country}".format(date=case['observation_date'], country=case['country'])
            if key in groups:
                if case['city']:
                    groups[key].country.cities.append(case['city'])

                groups[key].observation = groups[key].observation + Observation.from_dict(case)

            else:
                groups[key] = CaseObservation(date=case['observation_date'], country=Country.from_dict(case),
                                              observation=Observation.from_dict(case))
        return groups
