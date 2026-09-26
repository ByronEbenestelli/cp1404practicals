from prac_02.temperatures import convert_celsius_to_fahrenheit, convert_fahrenheit_to_celsius


def main():
    print("Convert celsius to fahrenheit? (C)",
          "Convert fahrenheit to celsius? (F)",
          "Quit (Q)",
          sep="\n")
    selection = input("\n").upper()
    while selection != "Q":
        if selection == "C":
            with open("temps_input.txt", "r") as in_file, open("temps_output.txt", "w") as out_file:
                for line in in_file:
                    print(convert_celsius_to_fahrenheit(float(line)), file=out_file)
        elif selection == "F":
            with open("temps_input.txt", "r") as in_file, open("temps_output.txt", "w") as out_file:
                for line in in_file:
                    print(convert_fahrenheit_to_celsius(float(line)), file=out_file)
        else:
            print("Invalid selection.")
        print("Convert celsius to fahrenheit? (C)",
              "Convert fahrenheit to celsius? (F)",
              "Quit (Q)",
              sep="\n")
        selection = input("\n").upper()
    print("Goodbye!!")


main()
