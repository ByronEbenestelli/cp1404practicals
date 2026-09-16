# print("Electricity bill estimator")
# price = float(input("Enter cents per kWh: ")) / 100  #Converts price from cents to dollars
# daily_use = float(input("Enter daily use in kWh: "))
# number_of_billing_days = int(input("Enter number of billing days: "))
# bill = price * daily_use * number_of_billing_days
# print(f"Estimated bill: ${bill:.2f}")

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
print("Electricity bill estimator 2.0")
tariff = input("Which tariff? 11 or 31 ")
while tariff != "11" and tariff != "31":
    print("Invalid input!")
    tariff = input("Which tariff? 11 or 31: ")
daily_use = float(input("Enter daily use in kWh: "))
number_of_billing_days = int(input("Enter number of billing days: "))
if tariff == "11":
    bill = TARIFF_11 * daily_use * number_of_billing_days
else:
    bill = TARIFF_31 * daily_use * number_of_billing_days
print(f"Estimated bill: ${bill:.2f}")
