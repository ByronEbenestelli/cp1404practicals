# ASCII Table
LOWER = 33
UPPER = 127


def main():
    character = input("Enter a character: ")
    ascii_code = ord(character)
    print(f"The ASCII code for {character} is {ascii_code}")
    ascii_number = get_valid_ascii_code()
    character_from_ascii = chr(ascii_number)
    print(f"The character for {ascii_number} is {character_from_ascii}")

    for i in range(LOWER, UPPER + 1):
        print(f"{i:>3}  {chr(i)}")


def get_valid_ascii_code():
    is_valid_input = False
    while not is_valid_input:
        try:
            ascii_number = int(input(f"Enter a number between {LOWER} and {UPPER}: "))
            while ascii_number < LOWER or ascii_number > UPPER:
                print(f"Value must be between {LOWER} and {UPPER}")
                ascii_number = int(input(f"Enter a number between {LOWER} and {UPPER}: "))
            is_valid_input = True
        except ValueError:
            print("Please enter a valid integer.")
    return ascii_number


main()
