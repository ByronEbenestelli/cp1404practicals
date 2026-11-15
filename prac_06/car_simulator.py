from prac_06.car import Car

MENU_OPTIONS = ["d) drive", "r) refuel", "q) quit"]


def main():
    print("Let's drive!")
    car = Car(input("Enter your car name: "), 100)
    print(car)
    display_menu()
    choice = input("Enter your choice: ").lower()
    while choice != "q":
        if choice == "d":
            drive_car(car)
        elif choice == "r":
            refuel_car(car)
        else:
            print("Invalid choice")
        print(f"\n{car}")
        display_menu()
        choice = input("Enter your choice: ").lower()
    print(f"Good bye {car.name}'s driver.")


def refuel_car(car):
    fuel = int(input("How many units of fuel do you want to add to the car? "))
    while fuel <= 0:
        print("Fuel amount must be >= 0")
        fuel = int(input("How many units of fuel do you want to add to the car? "))
    car.add_fuel(fuel)
    print(f"Added {fuel} units of fuel.")


def drive_car(car):
    distance = int(input("How many km do you wish to drive? "))
    while distance <= 0:
        print("Distance must be >= 0")
        distance = int(input("How many km do you wish to drive? "))
    starting_fuel = car.fuel
    car.drive(distance)
    ending_fuel = car.fuel
    total_distance = starting_fuel - ending_fuel
    if total_distance == distance:
        print(f"The car drove {distance}km.")
    else:
        print(f"The car drove {total_distance}km and ran out of fuel.")


def display_menu():
    print("Menu:")
    print("\n".join(MENU_OPTIONS))


main()
