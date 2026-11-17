"""
Guitars Practical
Estimated Time: 10 Mins
Actual Time: 18 Mins
"""
from prac_06.guitar import Guitar

print("My Guitars")
guitars = []
guitar_name = input("Name: ")
while guitar_name != "":
    guitar_year = int(input("Year: "))
    guitar_cost = float(input("Cost: "))
    guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
    print(f"{guitar_name} ({guitar_year}) : ${guitar_cost:.2f} added.\n")
    guitar_name = input("Name: ")
print("These are my guitars:")
for i, guitar in enumerate(guitars):
    category = "(vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year:4}) : worth $ {guitar.cost:10,.2f} {category}")
