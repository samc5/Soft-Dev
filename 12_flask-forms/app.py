# Gastric Bypass Train - Sam Cowan, Anna Fang, Sadi Nirloy
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

@app.route("/", methods=['GET'])
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
    #return render_template( 'login.html' )
    return render_template('response.html')


@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print("***DIAG: request.form ***")
    print(request.form)
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    return "Waaaa hooo HAAAH"  #response to a form submission

#The page for the new form
@app.route("/response", methods=['POST'])
def responding():
	message = "<h1>Ah, so it is the famed "
	message += request.form['username']
	message += ".</h1><h3> It is a pleasure to meet thee. Truly, I am humbled" + \
		" to be teaching one such as thyself.</h3>"
	message += "If you must know, you entered via the post method. You " + \
		"can tell by the URL above. One of the key differences between get and post is the difference is in the URL." + \
		"<br> The get method will cause your inputs and their corresponding keys from request.args to be added to the URL. But make no mistake, this does not mean your information is more secure here. " + \
		"A simple call to request.form will reveal the information that is not stored in request.args."
	
	message += "<br>The only other difference I may reveal to you now is in establishing a get form vs a post form." + \
		"<ul> <li>When creating the form in HTML, the attribute method=\"post\" <strong> must </strong> be added to create a post form." + \
		" Otherwise, that attribute is set to \"get\" as a default. method=\"get\" is allowed if you so desire.</li>"
	message += "<li>When setting up your .routes() for your Flask object, " + \
		"the receiving page of the information must be prepped. Since get is a default for the form, " + \
		"it is also set to the default of the page. However, an additonal argument can be added to " + \
		"decide the methods of input it should prepare for. <ul>"+ \
		"<li><strong>methods=['GET']</strong> explictly states the default settings of a route.</li>" + \
		"<li><strong>methods=['POST']</strong> prepares the route for the responses of a post form.</li>" + \
		"<li><strong>methods=['GET', 'POST']</strong> allows for either kind of form method to be used. If the form types didn't match up. You'll receive a MethodNotFound Error.</li>"

	message += "</ul>"
	message += "</ul>"
	return message
    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
