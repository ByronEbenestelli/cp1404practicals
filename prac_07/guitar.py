"""
Create a class, Guitar.
Estimated Time: 15 Mins
Actual Time: 9 Mins
"""
import datetime


class Guitar:
    """"""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise Guitar instance.

        name = string, name of guitar
        year = integer, when the guitar was made
        cost = float, how much the guitar cost
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        if self.year < other.year:
            return True
        else:
            return False

    def find_age(self):
        age = datetime.datetime.now().year - self.year
        return age

    def is_vintage(self):
        if self.find_age() >= 50:
            return True
        else:
            return False
