"""
A shop requires a small program that would allow them to quickly work out the total price for a number of items, each with different prices.

The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the screen.
"""

# Sample Output
# Number of items: 3
# Price of item: 100
# Price of item: 35.56
# Price of item: 3.24
# Total price for 3 items is $124.92

# Original Code
# number_of_items = int(input("Number of items: "))
# total_price = 0
# for i in range(number_of_items):
#     total_price += float(input("Price of item: "))
# if total_price > 100:
#     total_price = total_price * 0.9
# print(f"Total price for {number_of_items} items is ${total_price:.2f}")


# Added input validation loop
total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    total_price += float(input("Price of item: "))
if total_price > 100:
    total_price = total_price * 0.9
print(f"Total price for {number_of_items} items is ${total_price:.2f}")