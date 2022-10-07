# Blinking Holly Fountains - Gitae Park, Ravindra Mangar, Sam Cowan
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) # I think it will create a new flask app with the name of the file

@app.route("/") # I think the app will display the information of this file in the root 
def hello_world():
    print(__name__) # I think the file will print the name of the file in the terminal.
    return "No hablo queso!"  # I think the file will display "No hablo queso" to the webpage.

app.run()  # I think the webpage will render on the localhost IP
                
