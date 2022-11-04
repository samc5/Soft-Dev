"""

"""
from flask import Flask
from flask import session
from flask import render_template
from flask import request

app = Flask(__name__)

logins = {
    "gastric bypass train": "Heebiejeebies"
}

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/response", methods = ["POST", "GET"])
def response():
    return render_template("response.html")