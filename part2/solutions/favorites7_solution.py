# favorites7.py
import csv

# Open the CSV file from part1
with open("../../part1/favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    counts = {}
    
    # Count how many students chose each language
    for row in reader:
        favorite = row["language"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

# Print counts sorted alphabetically by language
for favorite in sorted(counts):
    print(f"{favorite}: {counts[favorite]}")