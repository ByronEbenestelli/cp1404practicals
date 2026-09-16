"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    grade = determine_grade(score)
    random_score = float(random.randint(0, 100))
    random_score_grade = determine_grade(random_score)
    print(f"User score {score} is {grade}.")
    if grade == "Excellent":
        print("You get a prize!")
    print(f"Random score {random_score} is {random_score_grade}.")


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
