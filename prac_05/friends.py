MENU_OPTIONS = ["Enter New Name and Address (E)", "Change an Address (C)", "Print address (P)", "Display menu (D)",
                "Quit (Q)"]


def main():
    name_to_address = {}
    display_menu()
    selection = input("Choose option: ").upper()
    while selection != "Q":
        if selection == "E":
            name = input("Enter name: ")
            address = input("Enter address: ")
            name_to_address[name] = address
        elif selection == "C":
            print(", ".join(list(name_to_address.keys())))
            name = input(
                "If your name is in above list, please enter it. Otherwise press ENTER to return to main menu.\n")
            while name != "":
                if name in name_to_address.keys():
                    address = input("Enter new address: ")
                    name_to_address[name] = address
                else:
                    print("Invalid name, please try again.")
                name = input(
                    "If your name is in above list, please enter it. Otherwise press ENTER to return to main menu.\n")
        elif selection == "P":
            name = input("What friend do you want to know the address of: ")
            try:
                print(f"{name} lives at {name_to_address[name]}.")
            except KeyError:
                print(f"{name} is not in your list of friends! :(")
        elif selection == "D":
            display_menu()
        else:
            print('Invalid menu option! Please try again.')
        selection = input("Choose option: ").upper()


def display_menu():
    for menu_option in MENU_OPTIONS:
        print(menu_option)


main()
