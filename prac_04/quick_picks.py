import random

MIN = 1
MAX = 45
NUMBERS_PER_LINE = 6


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    for line in range(number_of_quick_picks):
        quick_pick = []
        for item in range(NUMBERS_PER_LINE):
            random_value = random.randint(MIN, MAX)
            while random_value in quick_pick:
                random_value = random.randint(MIN, MAX)
            quick_pick.append(random_value)
        quick_pick.sort()
        for value in quick_pick:
            print(f"{value:>2}", end=" ")
        print()


main()

