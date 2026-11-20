"""
Project Management Prac
Time Estimate: 40 Mins
Actual Time: 11:20am
"""
from prac_07.project import Project

FILENAME = "projects.txt"
MENU_OPTIONS = ["(L)oad projects", "(S)ave projects", "(D)isplay projects", "(F)ilter projects by date",
                "(A)dd new project", "(U)pdate project", "(Q)uit"]


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    display_menu()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            incomplete_projects = [project for project in projects if project.percent_complete != 100]
            completed_projects = [project for project in projects if project.percent_complete == 100]
            incomplete_projects.sort()
            completed_projects.sort()
            print("Incomplete projects:")
            display_projects(incomplete_projects)
            print("Completed projects:")
            display_projects(completed_projects)
        elif choice == "F":
            pass
        elif choice == "A":
            print("Let's add a new project")
            name = input("Name: ")
            start_date = input("Start date (dd/mm/yy): ")
            priority = int(input("Priority: "))
            cost = float(input("Cost estimate: $"))
            percent_complete = int(input("Percent complete: "))
            projects.append(Project(name, start_date, priority, cost, percent_complete))
        elif choice == "U":
            display_projects(projects, True)
            project_choice = int(input("Project choice: "))
            print(projects[project_choice])
            try:
                percentage = int(input("New percentage: "))
                projects[project_choice].percent_complete = percentage
            except ValueError:
                pass
            try:
                priority = int(input("New priority: "))
                projects[project_choice].priority = priority
            except ValueError:
                pass
        else:
            print("Invalid menu option! Try again!")
        display_menu()
        choice = input(">>> ").upper()


def display_menu():
    for option in MENU_OPTIONS:
        print(option)


def load_projects(filename):
    projects = []
    with open(filename, "r", newline="") as in_file:
        in_file.readline()  # Ignore header row
        for row in in_file:
            row = row.strip().split("\t")
            project = Project(row[0], row[1], int(row[2]), float(row[3]), int(row[4]))
            projects.append(project)

    return projects


def display_projects(projects, with_index=False):
    if with_index:
        for index, project in enumerate(projects):
            print(index, project)
    else:
        for project in projects:
            print(project)


main()
