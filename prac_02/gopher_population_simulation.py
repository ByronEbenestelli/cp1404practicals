import random
from math import floor


def main():
    population_of_gophers = 1000
    print("Welcome to the Gopher Population Simulator!",
          f"Starting Population: {population_of_gophers}\n",
          sep="\n")

    number_of_years = get_valid_number_of_years()
    for year in range(number_of_years):
        pop_increase = round(random.uniform(0.1, 0.2) * population_of_gophers)
        pop_decrease = round(random.uniform(0.05, 0.25) * population_of_gophers)
        population_of_gophers += pop_increase - pop_decrease
        print(f"Year {year+1}",
              f"{pop_increase} were born.",
              f"{pop_decrease} died.",
              f"Population: {population_of_gophers}\n",
              sep="\n")



def get_valid_number_of_years():
    is_valid = False
    while not is_valid:
        try:
            number_of_years = int(input("How many years? "))
            is_valid = True
        except ValueError:
            print("Invalid input.")
    return number_of_years


main()
