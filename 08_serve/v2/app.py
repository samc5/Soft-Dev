# Blinking Holly Fountains - Gitae Park, Ravindra Mangar, Sam Cowan
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   # Where will this go? - in the terminal - when you refresh the webpage
    return "No hablo queso!"

app.run()
