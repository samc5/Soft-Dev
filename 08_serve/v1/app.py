# Blinking Holly Fountains - Ravindra Mangar, Gitae Park, Sam Cowan
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    #missing print(__name__), does not print file path.
    return "No hablo queso!"

app.run()

