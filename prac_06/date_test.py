from prac_06.date import Date

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
date = Date(day, month, year)
print(date)

change = int(input("Days: "))
while change != "":
    date.add_days(change)
    print(date)
    change = int(input("Days: "))

