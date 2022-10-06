# Blinking Holly Fountains - Ravindra Mangar, Gitae Park, Sam Cowan
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) # Create a new Flask app with the name of the file.

@app.route("/") # The app will display the information of this file in the root.
def hello_world():
    print(__name__) # The file will print the name of the path in the terminal.
    return "No hablo queso!"  # The file will display "No hablo queso!" to the webpage.

app.run()  # The webpage shall render on the localhost IP.
