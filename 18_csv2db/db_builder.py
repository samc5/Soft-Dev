"""
Sam Cowan, Anna Fang, Sadi Nirloy of Soup Shark
"""

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >
#Open a file as csv


#with open ("students.csv", newline=' ') as csvfile:
#For some reason, the one above does not work, despite being recommended in the example of the documentation
	#Create a reading class, like BufferedReader or Scanner
	#This reader is specialized in reading csvs into dicitonaries
	#As the DictReader reads the csvfile, the file is read in rows where each index is the value at the column
	#The column name is determined automatically here as the values of the first row
 
	#Printing reading only returns an address, but I suspect that the reading variable stores a list of dictionaries 
	#print(reading)

	#Continuing my lessThanThesis, we use the for each loop to grab each of the dictionaries in the list, and can then use the keys from the first row to access each value
	#for row in reading:
		#print(row["name"] + ": " + row["age"] + ", " + row["id"] + ";")
		
		#From testing multiple loops of reading
		#print("7")
		
		#Testing list of dicts
		#print(row.keys())
		#Results: keys of name, age, and id, all strings
		#Conclusion less than thesis can become hyperthesis: fact

		

	#Testing list structure
	#print(reading[0])
	#Result: DictReader not subscriptable
	#Conclusion: We have another viewing object, so we cannot access values via bracket notations.

	#Testing list of dict structure
	#for ree in reading:
	#	print(row.keys())
	#Nothing prints (???)
	#	print("5")
	#Nothing again
	#Conclusion: DictReader can only be looped through once I guess

	#Now that we did all that testing, we can move onto turning this list of dictionaries into a dictionary of lists
	#We could retain the list of dicts structure; it is easy to interchange between them, but I prefer it this way, with the info categorized by type. It also allows for easier overlapping of tables, as we can copy the entire values list of a category, instead of needing to loop through the entire dict
		#To explain what I mean, if we are given a bunch of raw data, meant to be turned into multiple tables, we'll want to store each column as one group so that multiple tables can easily copy that column
		#ie) copying students[names]

	#for row in reading:
		#for key in row.keys():
			#studentDict[key].append(row[key])
			#ERROR: the studentDict keys have not been decided yet. And I really want to automate this

	#It is also possible to skip the intermediate dictionary, and translate the csv into commands, but we run into the same issue of unautomated keys/categories
	#If I can find a way to isolate these keys of DictReader sans a loop, I could automate this well

	#Duh, there is the fieldnames variable, a list of the names of the columns. I can't believe I have the same amount of object permanence as a baby.
	#This field is handled automatically, and because of that I forgot about it completely and I needed to look at the actual documentation of DictReader to remember it -_-
	#print(reading.fieldnames)

	#Now, we are in business

	#Dictionary Implementation:
	#Establishing dictionary
	#for key in reading.fieldnames:
		#studentDict[key] = []
	#Filling Dict
	#for row in reading:
		#for key in row.keys():
			#studentDict[key].append(row[key])
		
	#print(studentDict)

	#Now I need to handle the commands using the dictionary
	#I'll attempt the direct way afterwards
	#Or we just ignore the dict? It may be easier. 
	#We have an issue where all the string need a set of quotation marks, but we have no way of automating that, but do we have to?
  # run SQL statement

with open ("students.csv") as csvfile:
	reading = csv.DictReader(csvfile)
	c.execute("create table if not exists students(name text, age int, id int);");
	
	for row in reading:
		additionCommand = "insert into students values("
		counter = 0;
		for key in reading.fieldnames:
			additionCommand += "\"" + str(row[key]) + "\""
			if (counter < len(reading.fieldnames) - 1):
				additionCommand += ", "
			counter += 1
		additionCommand += ");"
		#print (additionCommand)
		c.execute(additionCommand);

	c.execute("select * from students")	

with open ("courses.csv") as csvfile:
        reading = csv.DictReader(csvfile)
        c.execute("create table if not exists courses(code text, mark int, id int);");

        for row in reading:
                additionCommand = "insert into courses values("
                counter = 0;
                for key in reading.fieldnames:
                        additionCommand += "\"" + str(row[key]) + "\""
                        if (counter < len(reading.fieldnames) - 1):
                                additionCommand += ", "
                        counter += 1
                additionCommand += ");"
                #print (additionCommand)
                c.execute(additionCommand);

        c.execute("select * from courses")	
#==========================================================

db.commit() #save changes
db.close()  #close database


