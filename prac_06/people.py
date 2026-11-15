"""
Create list of Person instances.
"""
from operator import attrgetter

from prac_06.person import Person

people = []
first_name = input("First name: ")
while first_name != "":
    last_name = input("Last name: ")
    age = int(input("Age: "))
    people.append(Person(first_name, last_name, age))
    first_name = input("First name: ")

people.sort(key=attrgetter("age"))
print(f"{"Name":20}{"Age":5}")
for person in people:
    print(f"{" ".join((person.first_name, person.last_name)):20}{person.age:<5}")


