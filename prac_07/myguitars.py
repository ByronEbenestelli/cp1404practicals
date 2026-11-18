import csv

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    my_guitars = load_guitars()

    # Display my guitars
    display_guitars(my_guitars)

    # Display my guitars sorted by year
    my_guitars.sort()
    display_guitars(my_guitars)

    # Add guitars and display sorted by year
    add_guitars(my_guitars)
    my_guitars.sort()
    display_guitars(my_guitars)

    write_guitars(my_guitars)


def add_guitars(guitars):
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: "))
        guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
        print(f"{guitar_name} ({guitar_year}) : ${guitar_cost:.2f} added.\n")
        guitar_name = input("Name: ")


def load_guitars():
    my_guitars = []
    with open(FILENAME, "r", newline="") as in_file:
        in_file.readline()  # Skip header line
        reader = csv.reader(in_file)
        for row in reader:
            # Convert year to int and cost to float
            guitar = Guitar(row[0], int(row[1]), float(row[2]))
            my_guitars.append(guitar)
    return my_guitars


def write_guitars(guitars):
    with open(FILENAME, "w", newline="") as out_file:
        writer = csv.writer(out_file)
        for guitar in guitars:
            writer.writerow((guitar.name, guitar.year, guitar.cost))


def display_guitars(guitars):
    print("These are my guitars:")
    for guitar in guitars:
        print(guitar)
    print()


main()
