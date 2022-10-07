import time

'''
Working On It: Ravindra Mangar and Samantha Hua
SoftDev
K05 -- 06_py-csv -- Reading csv files and weighted randomness
2022-10-02
time spent: 1hr

DISCO:
    - random.choices(iter, weights=[]) returns a random value in the iter based on the different weights specified
    - next() allows you to skip a line while reading a csv file
    - dict_name.values() returns all of the values in the dictionary
QCC:
  - How can we approach weighted randomness without using random.choices()?
  - Is there an easier way to map out a function on all values in a dictionary?
  - Did we need to divide each value in the dictionary by the total? Would it have worked the same if we didn't?

HOW THIS SCRIPT WORKS:
    - Create an empty dictionary
    - Read the contents of the file inputted
    - Skip the first line in the csv file because it is the header
    - For each line in the file, save the occupation as the key in the dictionary and the percentage as the value associated with that key
    - Save the total percent by looking at the value associated with "Total"
    - For every value in the dictionary, divide it by the total so you get the percent in which it should show up
    - Set the value of "Total" to be 0 so it won't show up when you randomly pick a occupation
    - Pick a random occupation based on their weight
'''

import csv
import random

t0 = time.time()

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
print(time.time() - t0)
