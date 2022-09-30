import random
import csv


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
print(random_occupation)