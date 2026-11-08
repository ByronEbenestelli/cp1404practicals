def main():
    file_name = input("Enter filename: ")
    while file_name != "":
        try:
            print(f"{file_name} has {count_lines(file_name)} lines.")
        except FileNotFoundError:
            print(f"ERROR: {file_name} does not exist.")
        file_name = input("Enter filename: ")


def count_lines(file_name):
    with open(file_name, "r") as in_file:
        number_of_lines = 0
        for line in in_file:
            number_of_lines += 1
    return number_of_lines


main()
