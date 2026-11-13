import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
DETERMINER = "cv"

word_format = input("Input word format where % is a consonant, # is a vowel and any alphabetical characters will "
                    "be themselves. Example: %%ea%% could be greatly or hreajk: \n").lower()
word = ""
for kind in word_format:
    if kind == "%":
        word += random.choice(CONSONANTS)
    elif kind == "#":
        word += random.choice(VOWELS)
    elif kind in VOWELS or kind in CONSONANTS:
        word += kind

print(word)

random_word_length = int(input("How long for random word? "))
random_word_format = ""
random_word = ""
for i in range(random_word_length):
    random_word_format += random.choice(DETERMINER)
for kind in random_word_format:
    if kind == "c":
        random_word += random.choice(CONSONANTS)
    else:
        random_word += random.choice(VOWELS)

print(random_word)
