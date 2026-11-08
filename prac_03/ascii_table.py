# ASCII Table
LOWER = 33
UPPER = 127

character = input("Enter a character: ")
ascii_code = ord(character)
print(f"The ASCII code for {character} is {ascii_code}")
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
character_from_ascii = chr(ascii_number)
print(f"The character for {ascii_number} is {character_from_ascii}")
