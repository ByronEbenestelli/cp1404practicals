import csv

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    my_guitars = load_guitars()
    print("These are my guitars:")
    display_guitars(my_guitars)
    print("These are my guitars sorted:")
    my_guitars.sort()
    display_guitars(my_guitars)


def load_guitars():
    my_guitars = []
    with open(FILENAME, "r") as in_file:
        in_file.readline()  # Skip header line
        reader = csv.reader(in_file)
        for row in reader:
            # Convert year to int and cost to float
            guitar = Guitar(row[0], int(row[1]), float(row[2]))
            my_guitars.append(guitar)
    return my_guitars


def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)


main()
