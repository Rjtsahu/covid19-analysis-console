class Country(object):

    def __init__(self, country):
        self.country_name = country
        self.cities = []

    def __repr__(self):
        return self.country_name

    def __str__(self):
        return self.country_name

    @staticmethod
    def from_dict(row):
        country = Country(row['country'])
        country.cities = [row['city']] if row['city'] else []

        return country
