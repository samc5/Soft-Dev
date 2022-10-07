# your heading here

from flask import Flask
from numbercruncher import random_occupation

app = Flask(__name__) 

@app.route("/") 
def generate():
    for i in random_occupation("occupations.csv"):
      return i

app.run() 


'''
DISCO:

QCC:
0. 
1. 
2. 
3. 
4. 
5. 
...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''
