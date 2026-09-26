import random


def main():
    number_of_scores = get_valid_integer_input()
    out_file = open("results.txt", "w")
    for i in range(number_of_scores):
        random_score = random.randint(0, 100)
        random_score_result = determine_grade(random_score)
        print(f"{random_score} is {random_score_result}", file=out_file)
    out_file.close()

def get_valid_integer_input() -> int:
    is_valid = False
    while not is_valid:
        try:
            number_of_scores = int(input("Enter number of scores: "))
            is_valid = True
        except ValueError:
            print("Invalid input.")
    return number_of_scores


def determine_grade(score: float):
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
