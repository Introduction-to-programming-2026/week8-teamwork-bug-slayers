# favorites0_solution.py
import csv

with open("favorites.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)          # Skip the header row
    for row in reader:
        print(row[1])     # Print the second column of each row
