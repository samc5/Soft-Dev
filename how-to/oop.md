# how-to :: Use Object Oriented Programming in Python
---
## Overview
OOP allows us to assign common attributes (variables and methods) to a group of things, allowing us to use the same code instead of rewriting over and over for each object. It also lets us hide implementation details from the user (preventing them from destroying things like the mindless animals they are), and to create multiple methods (that do and take in different inputs) with the same name. 

To break it down into simple(r) terms: 
- Abstraction : separation of code and user
- Encapsulation: gathering up a bunch of methods and variables into one data structure
- Inheritance: Passing down the structure and methods of another class
- Polymorphism: Using a template to create multiple similar, but not exactly the same, objects 

### Estimated Time Cost: Depends on the program in question. 

### Prerequisites:

- You should have Python installed on your machine 
- Have a text-editor (atom, thonny, notepad, etc)
- You need an understanding of basic python syntax
    - Variables
    - Methods
    - Fundamental Datatypes (Integers, Floats, Characters, Booleans, Strings, Arrays)
- Decent File Management (Note that having multiple classes in a file is less frowned upon than in java)

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
**self**\
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
- Inherited classes are a construct in which a subclass or child of a parent class is created, with the same functionality as outlined in the parent class as well as additional or edited variables and/or methods
- This furthers the idea of reusing instead of rewriting code, as a nearly identical class does not need to be rewritten.
- Rules of Inheritance:
	- Method defined only in the parent class: Can be called by parent or child class.
	- Method defined only in the child class: Can be called by child but not parent
	- Method defined in both child and parent and called by a child, the child version will be used instead of the parent.
- Inheritance is extremely important in python because the language does not support method overloading, as in having multiple functions of the same name. As a replacement, subclasses can be used for method overriding - allowing for several methods of the same name
```
class ParentClass: 
	def __init__(self, var1, var2):
		self.var1 = var1
		self.var2 = var2
class ChildClass(ParentClass):
	pass
```
- The pass keyword will allow you to leave a class empty for whatever reason you want, useful for demo code like this.
- The child class will automatically inherit the \_\_init\_\_ function of its parent class.
- In order to create a child class's \_\_init\_\_ function, you can use super() to refer to the parent class, and call it's methods
```
class ParentClass: 
	def __init__(self, var1, var2):
		self.var1 = var1
		self.var2 = var2
class ChildClass(ParentClass):
	def __init__(self, var1, var2, extra1):
		super().__init__(var1, var2)
		self.extra1 = extra1
```
### Resources
[W3Schools](https://www.w3schools.com/python/python_classes.asp)
[Official Python Documentation for those with time](https://docs.python.org/3/tutorial/classes.html)

---

Accurate as of (last update): 2022-10-20

#### Contributors:  
Sam Cowan, Pd 7
Anna Fang, Pd 7
Sadi Nirloy, Pd 7

