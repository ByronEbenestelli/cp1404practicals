"""
Project Class
"""


class Project:
    def __init__(self, name="", start_date="", priority=0, cost=0.0, percent_complete=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.percent_complete = percent_complete

    def __str__(self):
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: {self.cost}, "
                f"completion: {self.percent_complete}%")

    def __lt__(self, other):
        if self.priority < other.priority:
            return True
        else:
            return False
