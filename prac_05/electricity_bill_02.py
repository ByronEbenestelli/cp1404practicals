# print("Electricity bill estimator")
# price = float(input("Enter cents per kWh: ")) / 100  #Converts price from cents to dollars
# daily_use = float(input("Enter daily use in kWh: "))
# number_of_billing_days = int(input("Enter number of billing days: "))
# bill = price * daily_use * number_of_billing_days
# print(f"Estimated bill: ${bill:.2f}")

tariff_to_percentage = {"11": 0.244618, "31": 0.136928, "42": 0.456743, "12": 0.213453, "98": 0.654353}
print("Electricity bill estimator 2.0")
tariff = input(f"Which tariff? {" or ".join(tariff_to_percentage.keys())}: ")
while tariff not in tariff_to_percentage.keys():
    print("Invalid input!")
    tariff = input(f"Which tariff? {" or ".join(tariff_to_percentage.keys())}: ")
daily_use = float(input("Enter daily use in kWh: "))
number_of_billing_days = int(input("Enter number of billing days: "))
bill = tariff_to_percentage[tariff] * daily_use * number_of_billing_days
print(f"Estimated bill: ${bill:.2f}")
