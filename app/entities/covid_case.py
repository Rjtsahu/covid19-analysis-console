class CaseObservation(object):

    def __init__(self, date, observation, country):
        self.observation_date = date
        self.observation = observation
        self.country = country

    @classmethod
    def get_csv_row_to_dict(cls, row):
        return {'observation_date': row[1], 'city': row[2], 'country': row[3], 'confirmed': row[5],
                'deaths': row[6], 'recovered': row[7]}

    def __str__(self):
        return "date : {date} | country : {country} | observation : [ {observation} ]".format(
            date=self.observation_date,
            country=self.country,
            observation=self.observation)


class Observation(object):

    def __init__(self):
        self.confirmed = 0
        self.deaths = 0
        self.recovered = 0

    def __repr__(self):
        return "Observations are confirmed: {confirmed} , deaths : {deaths} , recovered: {recovered}".format(
            confirmed=self.confirmed,
            deaths=self.deaths,
            recovered=self.recovered)

    def __str__(self):
        return " confirmed: {confirmed} | deaths : {deaths} | recovered: {recovered} ".format(
            confirmed=self.confirmed,
            deaths=self.deaths,
            recovered=self.recovered)

    def __add__(self, other):

        if isinstance(other, Observation):
            observation = Observation()
            observation.confirmed = self.confirmed + other.confirmed
            observation.deaths = self.deaths + other.deaths
            observation.recovered = self.recovered + other.recovered

            return observation

    @staticmethod
    def from_dict(row):

        def get_default(key):
            try:
                return int(row[key].split('.')[0])
            except KeyError or ValueError:
                return 0

        observation = Observation()
        observation.confirmed = get_default('confirmed')
        observation.deaths = get_default('deaths')
        observation.recovered = get_default('recovered')

        return observation
