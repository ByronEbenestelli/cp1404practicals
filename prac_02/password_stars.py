def main():
    minimum_password_length = set_minimum_password_length()
    password = get_valid_password(minimum_password_length)
    print_hidden_password(password)


def set_minimum_password_length():
    return int(input("Minimum Password Length: "))


def get_valid_password(minimum_password_length):
    password = input("Create Password: ")
    while len(password) < minimum_password_length:
        print("Invalid Password")
        password = input("Create Password: ")
    return password


def print_hidden_password(password):
    print("*" * len(password), end="")


main()
