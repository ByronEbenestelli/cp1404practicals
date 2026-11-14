"""
Wimbledon
Estimate: 40 minutes
Actual:  minutes
"""
import csv

FILENAME = "wimbledon.csv"


def main():
    """Load data file and print details about Wimbledon champions and countries."""
    countries, winners = load_file()
    winner_to_wins = process_winner_records(winners)
    display_records(countries, winner_to_wins)


def display_records(countries, winner_to_wins):
    """Display champions with number of wins and countries."""
    print("Wimbledon Champions:")
    for winner, wins in winner_to_wins.items():
        print(winner, wins)
    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def process_winner_records(winners):
    """Create dictionary of champions to number of wins."""
    unique_winners = sorted(set(winners))
    winner_to_wins = {}
    for unique_winner in unique_winners:
        winner_to_wins[unique_winner] = winners.count(unique_winner)
    return winner_to_wins


def load_file():
    """Load records in set of countries and list of winners."""
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        countries = set()
        winners = []
        for line in reader:
            countries.add(line[1])
            winners.append(line[2])
    return countries, winners


main()
