"""Score Menu"""


def main():
    print("(G)et a valid score (must be 0 - 100 inclusive)",
          "(P)rint result",
          "(S)how stars",
          "(Q)uit",
          sep="\n")
    selection = input("Selection: ").upper()
    while selection != "Q":
        if selection == "G":
            pass
        elif selection == "P":
            pass
        elif selection == "S":
            pass
        else:
            print("Invalid selection. Try again.")
        print("(G)et a valid score (must be 0 - 100 inclusive)",
              "(P)rint result",
              "(S)how stars",
              "(Q)uit",
              sep="\n")
        selection = input("Selection: ").upper()
    "Goodbye!"


main()
