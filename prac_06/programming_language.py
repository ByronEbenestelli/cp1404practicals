"""
Programming Language Class
Time Estimate: 30 Mins
Actual Time: 19 Mins
"""


class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgammingLanguage instance.

        name: string, name of programming language
        typing: string, Static or Dynamic
        reflection: boolean
        year: integer, year the programming language was invented
        """
        if typing != "Static" and typing != "Dynamic":
            raise ValueError("typing must be either Static or Dynamic.")
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        if self.typing == "Static":
            return False
        else:
            return True
