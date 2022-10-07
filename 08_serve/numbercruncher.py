import csv
import random

def random_occupation(filename):
    # declare an empty dictionary
    occupations = {}

    # read csv file
    with open(filename, "r") as f:
        f_read = csv.reader(f)
        # to skip the header of the csv file
        next(f_read)

        for line in f_read:
          # made the value associated with each key a float so that it can be used in weights
          occupations[line[0]] = float(line[1])
        total = occupations["Total"]

        for key in occupations.keys():
            # divide by total to get a percentage
            occupations[key] = occupations[key]/total
        #print(occupations)
        occupations["Total"] = 0
        return random.choices(list(occupations.keys()), weights = occupations.values())

print(random_occupation("occupations.csv"))
