x = int(input("Enter value for x: "))
y = int(input("Enter value for y: "))
menu = (f"1. Show the even numbers from {x} to {y}",
        f"2. Show the odd numbers from {x} to {y}",
        f"3. Show the squares of the numbers from {x} to {y}",
        "4. Exit the program")
for i in menu:
    print(i)
choice = int(input("Make selection: "))
while choice != 4:
    if choice == 1:
        if x % 2 == 0:
            for i in range(x, y + 1, 2):
                print(i, end=" ")
        else:
            for i in range(x + 1, y + 1, 2):
                print(i, end=" ")
    elif choice == 2:
        if x % 2 != 0:
            for i in range(x, y + 1, 2):
                print(i, end=" ")
        else:
            for i in range(x + 1, y + 1, 2):
                print(i, end=" ")
    elif choice == 3:
        for i in range(x,y):
            print(i*i, end=" ")
    else:
        print("Invalid choice!")
    print()
    for i in menu:
        print(i)
    choice = int(input("Make selection: "))
print("Goodbye!")
