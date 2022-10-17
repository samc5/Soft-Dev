# Blinking Holly Fountains! - Ravindra Mangar, Gitae Park, Sam Cowan
# K11: Form(s) Like Voltron
# SoftDev
# 14-10-22
# time spent: tbd hrs

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

@app.route("/") #, methods=['GET', 'POST'])
#methods PREDICTION: present these strings in HTML?
#methods RUNNING: don't seem to do anything?

def disp_loginpage():
    print("\n\n\n") #no difference if commented out or not, probably for the
                    #browser
    #print("***DIAG: this Flask obj ***") #***DIAG: this Flask obj ***
    #print(app) #PREDICTION: returns app name? RUNNING: <Flask 'app'>
    #print("***DIAG: request obj ***")
    #print(request) #PREDICTION: returns IP address? RUNNING:
    #<Request 'http://127.0.0.1:5000/' [GET]> (is this a GET request?)
    #print("***DIAG: request.args ***")
    #print(request.args) #ImmutableMultiDict([]) (what is that?)
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username']) #ERROR, are we even inputted args on
    #the view page?
    #print("***DIAG: request.headers ***")
    #print(request.headers) #returns a LOT of info, including OS, browser,
    #markdown language that is current being displayed, etc.
    return render_template( 'login.html' )


@app.route("/auth") # , methods=['GET', 'POST'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    return "Waaaa hooo HAAAH"  #response to a form submission


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
