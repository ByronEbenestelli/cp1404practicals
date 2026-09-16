for i in range(1, 21, 2):
    print(i, end=' ')
print()

""" Question a """
for i in range(0, 101, 10):
    print(i, end=" ")
print()

""" Question b """
for i in range(1, 20, -1):
    print(i, end=" ")
print()

""" Question c """
number_of_stars = int(input("How many stars? "))
print(f"Number of stars: {number_of_stars}")
print("*" * number_of_stars)
print()

""" Question d """
number_of_lines = int(input("How many lines? "))
for n in range(number_of_lines):
    print("*" * (n+1))
print()
