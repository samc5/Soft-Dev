#  Blinking Holly Fountains - Ravindra Mangar, Gitae Park, Sam Cowan
#  SoftDev
#  Oct 2022
#  Time Spent: 1 hrs

from flask import Flask
from numbercruncher import random_occupation
import csv

app = Flask(__name__) 

@app.route("/") 
def generate():
    csv_file = ""
    with open("occupations.csv", "r") as f:
      f_read = csv.reader(f)
      for row in f_read:
        if row[0] == "Total":
          pass
        elif row[0] == "Job Class":
          pass
        else:
          csv_file += f'{row[0]} (<a href="{row[2]}">{row[0]}</a>)<br>'
    for i in random_occupation("occupations.csv"):
      return f"Blinking Holly Fountains - Ravindra Mangar, Gitae Park, Sam Cowan<br><br>Congrats! You are now destined to forever be working in: {i}<br><br>{csv_file}"

app.run() 


'''
DISCO:
  - <br> instead of r"\n"
  - import individual functions from a python file

QCC:
0. Does any HTML work in the return window? Can you insert a HTML file there?

INVESTIGATIVE APPROACH:
1. Import csv
2. Follow the flask model (app.route("/"), app.run(), etc.)
3. Import our random occupations function from numbercruncher.py and run it
4. Open the occupations.csv file and turn its occupations into strings
5. Return one string contains all the inputs, separated by <br>
'''
