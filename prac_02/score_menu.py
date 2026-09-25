"""Score Menu"""
from prac_02.score import determine_grade


def main():
    print("(G)et a valid score (must be 0 - 100 inclusive)",
          "(P)rint result",
          "(S)how stars",
          "(Q)uit",
          sep="\n")
    selection = input("Selection: ").upper()
    while selection != "Q":
        if selection == "G":
            score = get_valid_score()
        elif selection == "P":
            try:
                print(determine_grade(score))
            except NameError:
                print("Please select score first.")
        elif selection == "S":
            try:
                print("*" * score)
            except NameError:
                print("Please select score first.")
        else:
            print("Invalid selection. Try again.")
        print("(G)et a valid score (must be 0 - 100 inclusive)",
              "(P)rint result",
              "(S)how stars",
              "(Q)uit",
              sep="\n")
        selection = input("Selection: ").upper()
    print("Goodbye!")


def get_valid_score():
    score = int(input("Select score: "))
    while score < 0 or score > 100:
        print("Invalid score.")
        score = int(input("Select score: "))
    return score


main()
