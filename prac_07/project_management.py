"""
Project Management Prac
Time Estimate: 40 Mins
Actual Time:
"""

FILENAME = "projects.txt"
MENU_OPTIONS = ["(L)oad projects", "(S)ave projects", "(D)isplay projects", "(F)ilter projects by date",
                "(A)dd new project", "(U)pdate project", "(Q)uit"]


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    display_menu()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid menu option! Try again!")
        display_menu()
        choice = input(">>> ").upper()


def display_menu():
    for option in MENU_OPTIONS:
        print(option)


def load_projects(filename):
    return True


main()
