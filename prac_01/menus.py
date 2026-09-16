"""
Simple menu-driven program
"""

name = input("Enter name: ")
menu = ("(H)ello", "(G)oodbye", "(Q)uit")
for i in menu:
    print(i)
choice = input()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    for i in menu:
        print(i)
    choice = input()
print("Finished")
