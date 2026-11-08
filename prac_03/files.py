# 1
name = input("What is your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2
in_file = open("name.txt", "r")
name = in_file.read().strip()
print(f"Hi {name}!")

# 3
with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline().strip())
    second_number = int(in_file.readline().strip())
    solution = first_number + second_number
    print(solution)

# 4
with open("numbers.txt", "r") as in_file:
    total = 0
    for line in in_file:
        total += int(line)
    print(total)
