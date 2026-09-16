"""Creates a user password"""


def main():
    """Takes user input for minimum password length and validates password to fit this requirement"""
    minimum_password_length = set_minimum_password_length()
    password = get_valid_password(minimum_password_length)
    print_hidden_password(password)


def set_minimum_password_length():
    """Sets minimum password length"""
    return int(input("Minimum Password Length: "))


def get_valid_password(minimum_password_length):
    """Gets valid password"""
    password = input("Create Password: ")
    while len(password) < minimum_password_length:
        print("Invalid Password")
        password = input("Create Password: ")
    return password


def print_hidden_password(password):
    """Prints *'s equal to length of password"""
    print("*" * len(password), end="")


main()
