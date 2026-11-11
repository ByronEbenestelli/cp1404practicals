strings = []
string = input("Enter string: ")
while string != "":
    strings.append(string)
    string = input("Enter string: ")

repeated_strings = set()
for string in strings:
    if strings.count(string) > 1:
        repeated_strings.add(string)

if repeated_strings:
    print(f"Strings repeated: {" ".join(repeated_strings)}")
else:
    print("No repeated strings entered")
