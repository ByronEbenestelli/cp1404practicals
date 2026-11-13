"""
Emails
Estimate: 20 minutes
Actual:   25 minutes
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        is_name = input(f"Is your name {name}? (Y/n) ").upper()
        if is_name != "Y" and is_name != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    words = email.split("@")[0].split(".")
    for index, word in enumerate(words):
        letters = [letter for letter in word]
        letters[0] = letters[0].upper()
        words[index] = "".join(letters)
    name = " ".join(words)
    return name


main()
