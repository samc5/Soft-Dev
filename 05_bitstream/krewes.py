""" 
Jacob Guo, Sam Cowan
SoftDev
05_bitstream
2022-09-28
time spent: 1.5 hours

DISCO:
    - Using list() to typecast the dictionary keys list into a list because for some reason x = dict_name.keys() is not a list
QCC:
    - n/a

OPS SUMMARY:
-.read() the file into a string
-.split() the file by "@@@" to make truples 
-then .split() again by "$$$" and get the first element of that list for the period
-make the next indices a dictionary: index a key and the last index its corresponding value
-add that new dictionary into the respective period's value list with krewesNew[pd].update(newDict)
-make a helper function, newRandomPd(dict), that uses recursion to select a random period which has 
 at least one devo, preventing an error coming from a period having no devos
-randomly select a devo from that period
-grab the devo's ducky_name
-return the Devo name, period, and ducky name concatenated
"""

import random
import math

# krewes = {2: ["hwang30", "wliu30", "iyeung30"],
#           7: ["dchen30", "dakhmedova30", "scowan30"],
#           8: ["sho30", "dhe30", "mmori30"]
#           }

# krewes = {
#            2: ["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY"], 
#            7: ["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"],
#            8: ["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "wanying"]
#          }

krewesNew = {
            2: {},
            7: {},
            8: {}
}


def chooseDevoWithInt():
    randomPd = chooseRandomPd()
    print("Random Period: ", randomPd)
    data = krewes[randomPd]
    return data[random.randint(0, len(data) - 1)]

def chooseRandomPd():
    return random.choice([2, 7, 8])

def chooseDevoWithChoice():
    randomPd = chooseRandomPd()
    print("Random Period: ", randomPd)
    data = krewes[randomPd]
    return random.choice(data)

def chooseDevoWithRandom():
    periods = [2, 7, 8]
    randomPd = periods[math.floor(random.random() * 3)]
    print("Random Period: ", randomPd)
    data = krewes[randomPd]
    return data[math.floor(random.random() * len(data))]

def split_krewes():
    krewes_file = open("krewes.txt", "r")
    read_file = krewes_file.read()
    krewes_truple = read_file.split("@@@")
    for i in range(len(krewes_truple)):
        double_split = krewes_truple[i].split("$$$")
        krewesNew[int(double_split[0])].update({double_split[1]: double_split[2]})
    pd = newRandomPd(krewesNew)
    dict_index = math.floor(random.random() * len(krewesNew[pd]))
    rand_name = list(krewesNew[pd].keys())[dict_index]
    rand_ducky = krewesNew[pd][rand_name]
    print(rand_name + ", " + str(pd) + ", " + rand_ducky)

def newRandomPd(dict):
    if dict:
        pd = random.choice(list(dict.keys()))
    if len(dict[pd]) == 0:
        del dict[pd]
        return newRandomPd(dict)
    return pd



# print("RANDOM.RANDINT:")
# print("Random Devo: ", chooseDevoWithInt())
# print("\nRANDOM.CHOICE:")
# print("Random Devo: ", chooseDevoWithChoice())
# print("\nRANDOM.RANDOM:")
# print("Random Devo: ", chooseDevoWithRandom())

# print(read_file)
# print(krewes_truple)
split_krewes()