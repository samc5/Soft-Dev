# K19 Notes
## DISCOS
### Setting up a session from an HTML form
```
session[key] = request.<form or args>[key]
```
### This only works for when key exists with in the request. You'll need try and excepts for when things go wrong.
```
return redirect(<route path>)
#This allows you to have a route that can loop back to a previous page
# Useful for creating changes in the variables in python before reloading a page
```
## QCC
### How can I rename the submit button of a form?
### Or at the very least, create a button that can lead to a new page or run a python method?
