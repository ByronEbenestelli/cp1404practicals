"""
Test the Guitar class.
Estimated Time: 10 Mins
Actual Time: 9 Mins
"""

from prac_06.guitar import Guitar

guitar = Guitar("Gibson L-5 CES", 1922, 16035.4)
another_guitar = Guitar("Another Guitar", 2013)
old_guitar = Guitar("50 Year Old Guitar", 1976)

print(f"{guitar.name} find_age() - Expected 104. Got {guitar.find_age()}")
print(f"{another_guitar.name} find_age() - Expected 13. Got {another_guitar.find_age()}")
print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")
print(f"{old_guitar.name} is_vintage() - Expected True. Got {old_guitar.is_vintage()}")
print(guitar)
