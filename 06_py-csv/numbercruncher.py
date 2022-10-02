"""
Super Jesus: Jacob Guo, Sam Cowan
SoftDev
06_py-csv
2022-10-03
time spent: 1.5 hours

DISCO:
    - built-in csv library can be used to read and write csvs
    - random.choices() is an easy way to make a random weighted choice
QCC:
    - How exactly does random.choices() work? We originally used it but didnt't feel fully comfortable explaining it

OPS SUMMARY:
    - used .open() to make csv file into a variable, and instead of .read() used csv.reader() to make a reader object of the csv
    -iterated through reader using a for loop, filling up a dictionary with the keys being occupations and the values a list of pertinent numbers - the percent of people with them, the low range for a random number in order to return this occupation, and the high range.
    - Each job has its own weight, so it has its own probability of being picked. We picked a number from 0 to 99.8, using random.uniform(0, 99.8), which is the total percentage of jobs.
    -  Our method of choosing jobs through weight was adding the weights and having a floor and ceiling value to compare the random number to for each job. By saving the sum, we can use it as the floor value for the next job.
    - Example of how we randomly choose a job based on the weights: J_1 = 6%, J_2 = 9, J_3 = 50%, etc. If I got a number 14, I would compare it to the floor and ceiling of each job (which is a bit inefficient). For J_1,whose ceilings are 0 to 6, I would check 0 < 14 < 6, which is false. Then, J_2, whose ceilings are 6 to 15, 6 < 14 < 15.This is true, so I return J_2
    - As was said before, for each entry in the jobs dictionary, we made the corresponding values a list. I scanned through them after picking the random number, and checked just like in the example above. And then we returned the job that the random number was between. 




"""

import random
import csv

def occ_chooser():
    occupations = open("occupations.csv","r")
    reader = csv.reader(occupations, delimiter = ',')
    oc_dict = {}
    sum = 0
    for row in reader:
        if row[1] != "Percentage":
            if row[0] != "Total":
                oc_dict.update({row[0] : [float(row[1]), sum, sum + float(row[1])] })
                sum += float(row[1])
    picker = random.uniform(0, 99.8)
    for e in oc_dict:
        percents = oc_dict[e]
        if picker >= percents[1] and picker <= percents[2]:
            return e
    
sum = 0
# for e in range(1000):
#     if(occ_chooser()) == "Office and administrative support":
#         sum += 1
# print(sum)
