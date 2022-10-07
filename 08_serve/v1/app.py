# Blinking Holly Fountains - Gitae Park, Ravindra Mangar, Sam Cowan
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    # missing print(__name__) - it won't print in the terminal but in the webpage the result doesn't change
    return "No hablo queso!"

app.run()
