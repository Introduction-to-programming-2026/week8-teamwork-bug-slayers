# favorites3.py
# Task: Same as favorites2 but print directly without a named variable.
#       One-liner inside the loop: print(row["language"])
#
# This version is more concise. favorites2 is more readable.
# Neither is "wrong" — it depends on the situation.

import csv

# Open CSV one folder up
with open("../favorites.csv", "r") as file:
    reader = csv.DictReader(file)  # row is a dictionary
    for row in reader:
        print(row["language"])  # print directly
