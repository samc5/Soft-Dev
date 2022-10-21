# how-to :: Use Object Oriented Programming in Python
---
## Overview
OOP allows us to assign common attributes (variables and methods) to a group of things, allowing us to use the same code instead of rewriting over and over for each object. It also lets us hide implementation details from the user (preventing them from destroying things like the mindless animals they are), and to create multiple methods (that do and take in different inputs) with the same name. 

To break it down into simple terms: 
- Abstraction 
- Encapsulation 
- Inheritance 
- Polymorphism 

### Estimated Time Cost: Depends on the program in question

### Prerequisites:

- You should have Python installed on your machine 
- Have a text-editor (atom, thonny, notepad, etc)
- You need an understanding of basic python syntax
    - Variables
    - Methods
    - Fundamental Datatypes (Integers, Floats, Characters, Booleans, Strings, Arrays)
- Decent File Management

### Building Python Objects:
**class keyword**
This word "class" is a keyword in Python to indicate that the next variable is a class. 
Syntax:
```
class ClassName:
```
** \_\_init\_\_ **
The \_\_init\_\_ function is the constructor for the class. Any parameters given to the \_\_init\_\_ can be used as fields of the class
```
class ClassName:
	def __init__(self, var1, var2): #There can be any number of parameters, as long as it is more than one
		self.var1 = var1
		self.var2 = var2
```
After creating this function, you can create instances of objects:
```
some_variable = ClassName(arg1, arg2) #Note the number of arguments, continue reading
```
**self**
The self parameter kind of doesn't exist. When any class method is being made, the very first parameter represents that instance of the class, and can be named anything. When that function is called, that parameter is automatically filled in, so the user provides 1 less argument than the number of parameters.
**\_\_str\_\_**
The \_\_str\_\_ function is the toString method, if you remember Java classes. The string that this method returns will be used to when the class is printed and converted into a string.
```
class ClassName:
	def __init__(self, var1):
		self.var1 = var1
	def __str__(self):
		return (str(self.var1))
```
**Basic Example**
```
class Fighter:
	def __init__(uhhhhh, name, strength, speed):
		uhhhhh.name = name
		uhhhhh.strength = strength
		uhhhhh.speed = speed
	def exercise(xdxd, hours): #Note the different name for the self parameter. That doesn't matter
		xdxd.strength += hours
		xdxd.speed += hours
	def __str__(mememe):
		message = mememe.name + ": " + \
			"Strength: " + str(mememe.strength) + ", " + \
			"\tSpeed: " + str(mememe.speed)

Lee = Fighter("Bruce", 100, 100)
print(Lee)
Lee.exercise(25)
print(Lee)
```
### Class Inheritance:


### Resources
* thing1
* thing2

---

Accurate as of (last update): 2022-mm-dd

#### Contributors:  
Sam Cowan, Pd 7
Anna Fang, Pd 7
Sadi Nirloy, Pd 7

_Note: the two spaces after each name are important! ( <--burn after reading)  _
