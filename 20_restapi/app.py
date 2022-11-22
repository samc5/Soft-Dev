"""
TNPG: Super Jesus
Jacob Guo, Sam Cowan
SoftDev
K20 -- Rest APIs and HTTP Requests
2022-11-21
time spent:  -->
"""

from flask import Flask, render_template, request
import requests
app = app = Flask(__name__)      
@app.route("/", methods = ["POST", "GET"])                   
def display():
    file = open("key_nasa.txt", "r")
    str = file.read()
    file.close()
    url = f'https://api.nasa.gov/planetary/apod?api_key={str}'
    print(url)
    r = requests.get(url)
    print(r.headers)
    print(r.text)
    data = r.json()
    img = data['url']
    exp = data['explanation']
    # print(data['url'])
    # print(data['explanation'])
    return render_template("main.html", image = img, explanation = exp)

if __name__ == "__main__": 
    app.debug = True                                                                                                        
    app.run()      