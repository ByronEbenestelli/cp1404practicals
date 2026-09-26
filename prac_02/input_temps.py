import random

is_valid = False
while not is_valid:
    try:
        number_of_temps = int(input("How many temps do you want? "))
        is_valid = True
    except ValueError:
        print("Invalid input.")
out_file = open("temps_input.txt", "w")
for i in range(number_of_temps):
    print(round(random.uniform(-200, 200), 5), file=out_file)
out_file.close()
