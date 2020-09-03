"""guitar class for prac_06"""


class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        """initialises the Guitar class"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : {}".format(self.name, self.year, self.cost)

    def get_age(self):
        age = 2020 - self.year
        return age

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False
