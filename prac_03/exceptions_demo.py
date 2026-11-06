"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When input cannot be converted to integer
2. When will a ZeroDivisionError occur? When denominator equals 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:  # When input cannot be converted to integer
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
