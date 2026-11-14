import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
DETERMINER = "cv"


def main():
    word_format = input("Input word format where c is a consonant, v is a vowel and any alphabetical characters will "
                        "be themselves. Example: cceacc could be greatly or hreajk: \n").lower()
    while not is_valid_format(word_format):
        print("Invalid format. Please try again.")
        word_format = input(
            "Input word format where c is a consonant, v is a vowel and any alphabetical characters will "
            "be themselves. Example: cceacc could be greatly or hreajk: \n").lower()

    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        elif kind == "v":
            word += random.choice(VOWELS)
        elif kind in VOWELS or kind in CONSONANTS:
            word += kind

    print(word)


def is_valid_format(word_format):
    for letter in word_format:
        if letter not in DETERMINER:
            return False
    return True


main()
