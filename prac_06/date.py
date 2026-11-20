"""
Date class
"""
MONTHS_WITH_31_DAYS = [1, 3, 5, 7, 8, 10, 12]
MONTHS_WITH_30_DAYS = [4, 6, 9, 11]
MONTHS_WITH_28_DAYS = [2]


class Date:
    def __init__(self, day=0, month=0, year=0):
        if month < 1 or month > 12:
            raise ValueError("Invalid month.")
        if month in MONTHS_WITH_31_DAYS and day > 31:
            raise ValueError("Invalid day for this month.")
        elif month in MONTHS_WITH_30_DAYS and day > 30:
            raise ValueError("Invalid day for this month.")
        elif month in MONTHS_WITH_28_DAYS and day > 28:
            raise ValueError("Invalid day for this month.")
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day},{self.month},{self.year}"

    def add_days(self, n=0):
        while n + self.day > 28 and n != 0:
            if self.month in MONTHS_WITH_31_DAYS and n + self.day > 31:
                n -= 31 - self.day
                self.day = 0
                if self.month == 12:
                    self.year += 1
                    self.month = 1
                else:
                    self.month += 1
            elif self.month in MONTHS_WITH_31_DAYS:
                self.day += n
                n = 0
            elif self.month in MONTHS_WITH_30_DAYS and n + self.day > 30:
                n -= 30 - self.day
                self.month += 1
                self.day = 0
            elif self.month in MONTHS_WITH_30_DAYS:
                self.day += n
                n = 0
            elif self.month in MONTHS_WITH_28_DAYS and n + self.day > 28:
                n -= 28 - self.day
                self.month += 1
                self.day = 0
        self.day += n
