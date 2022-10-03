# your heading here

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:

QCC:
0. python def object init
1. base directory in file system (cd /)
2. I suppose it will print to app, whatever it is. (Actually will print to console)
3. Will print whatever was defined as __name__ (Probably something defined within flask) - (actually __main__)
4. It will print to the webpage but not the console. because I saw it with my very eyes (prints to the / route on localhost defined earlier)
5. Never seen it 
...

INVESTIGATIVE APPROACH:
    Tried running the code and clicking the link to the generated webpage, then understanding what the input was saying based on the output
'''