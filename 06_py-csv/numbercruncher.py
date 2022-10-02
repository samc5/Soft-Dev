import random
import csv
"""




"""


def rand_occupation():
    occupations = open("occupations.csv","r")
    reader = csv.reader(occupations, delimiter = ',')

    oc_dict = {}
    for row in reader:
        if row[1] != "Percentage":
            if row[0] != "Total":
                oc_dict.update({row[0] : float(row[1])})


    keys = list(oc_dict.keys())
    values = list(oc_dict.values())

    random_occupation = random.choices(population = keys,weights = values, k = 1)
    return random_occupation

count = 0
for i in range(1000):
    if rand_occupation()[0] == "Farming, fishing and forestry":
        count += 1
print(count)