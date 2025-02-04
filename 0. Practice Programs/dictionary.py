#python dictionary.py

'''
	- Dictonaries are used to store data values in key:value pairs.
	- A disctonary is a collection which is ordered*, changeable and do not allow duplicates.
	- Dictonaries are written with curly brackets, and have keys and values:
'''

print("\nCreate and print a dictionary : \n")
thisdict1 = {
	"brand" : "Ford",
	"model" : "Mustang",
	"year" : 1964
}
print(thisdict1)	#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

'''
	- Dictonary Items : Are ordered, changeable and do not allow duplicates.
	- Are presented in key:value pairs, and can be referred to by suing the key name.
'''

print("\nPrint the 'brand' value of the dictionary : \n")
print(thisdict1["brand"])	#Ford

#Duplicates Not Allowed : 

print("\nDuplicate values will overwrite existing values : \n")
thisdict2 = {
	"brand" : "Ford",
	"model" : "Mustang",
	"year" : 1964,
	"year" : 2020
}
print(thisdict2)	#{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

#Dictonary Length : Use the len() function:

print("\nPrint the number of items in the dictionary : \n")
print(len(thisdict2))	#3

#Dictonary Items - Data Types : 
print("\nString, int, boolean, and list data types : \n")
thisdict3 = {
	"brand" : "Ford",
	"electric" : False,
	"year" : 1964,
	"colors" : ["red", "white", "blue"]
} 
print(thisdict3) #{'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}

#type() : From python's perspective, dictonaries are defined as objects with the data type 'dict'.
#<class 'dict'>

print(type(thisdict1)) #<class 'dict'>

#The dict() Constructor : It is also possible to use dict() constructor to make a dictonary.

print("\nUsing the dict() method to make a dictionary : \n")
thisdict4 = dict(name = "John", age = 36, country = "Norway")
print(thisdict4)	#{'name': 'John', 'age': 36, 'country': 'Norway'}

#Python Collection [Arrays] : There are four collection data types in python.
#1. List	2. Tuple	3. Set		4. Dictonary 

#Accessing Items : Access the items of a dictonary by referring to its key name, inside square brackets:

print("\nGet the value of the 'model' key 1st step : \n")
thisdict5 = {
	"brand" : "Ford",
	"model" : "Mustang",
	"year" : 1964
}
x = thisdict5["model"] 
print(x) #Mustang

#There is also a method called get() that will give you the same result:

print("\nGet the value of the 'model' key 2nd step : \n")
x = thisdict5.get("model") 
print(x) #Mustang

#Get keys : The keys() method will return a list of all the keys in the dictonary.

print("\nGet a list of the keys : \n")
x = thisdict5.keys()
print(x) #dict_keys(['brand', 'model', 'year'])

'''
	- The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary 
	will be reflected in the keys list.
'''

car1 = {
	"brand" : "Ford", 
	"model" : "Mustang",
	"year" : 1964
}

x = car1.keys()
print("\n#Before the change : \n")
print(x)  	#dict_keys(['brand', 'model', 'year'])

car1["color"] = "white"
print("\n#After the change : \n")
print(x) 		#dict_keys(['brand', 'model', 'year', 'color'])


#Get Values : values() method will return a list of the values in the dictonary.

print("\nGet a list of the values : \n")
x = thisdict1.values() 
print(x)	#dict_values(['Ford', 'Mustang', 1964])

'''
	- The list of the values is a view of the dictionary, meaning that any changes done 
	to the dictionary will be reflected in the values list.
'''

print("\nMake a change in the original dictonary, and see that the values list gets updates as well : \n")

car2 = {
	"brand" : "Ford", 
	"model" : "Mustang",
	"year" : 1964
}

x = car2.values()

print("\nBefore the change : \n")
print(x) #dict_values(['Ford', 'Mustang', 1964, 'white'])

print("\nAfter the change : \n")
car2["year"] = 2020
print(x) #dict_values(['Ford', 'Mustang', 2020, 'white'])

print("\nAdd a new item to the original dictonary, and see that the values list gets updated as well : \n")

car3 = {
	"brand" : "Ford", 
	"model" : "Mustang",
	"year" : 1964
}

x = car3.values()
print("\nBefore the change : \n")
print(x)	#dict_values(['Ford', 'Mustang', 1964])

print("\nAfter the change : \n")
car3["color"] = "red"
print(x)	#dict_values(['Ford', 'Mustang', 1964, 'red'])

#Get Items : The items() method will return each item in a dictonary, as tuples in a list.

print("\nGet a list of the key:value pairs : \n")

x = thisdict1.items()
print(x) #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

'''
	-The returned list is a view of the items of the dictionary, meaning that any changes done 
	to the dictionary will be reflected in the items list.
'''

print("\nMake a change in the original dictionary, and see that the items list gets updated as well :\n")

car4 = {
	"brand" : "Ford", 
	"model" : "Mustang",
	"year" : 1964
}

x = car4.items()
print("\nBefore the change : \n")
print(x) #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

print("\nAfter the change : \n")
car4["year"] = 2020
print(x)	#dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])

print("\nAdd a new item to the original dictionary, and see that the items list gets updated as well :\n")

car5 = {
	"brand" : "Ford", 
	"model" : "Mustang",
	"year" : 1964
}

x = car5.items()

print("\nBefore the change : \n")
print(x) #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

print("\nAfter the change : \n")
car5["color"] = "red"
print(car5) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

#Check if key Exists : Use the 'in' keyword :

if "model" in thisdict1:
	print("Yes, 'model' is one of the keys in the thisdict1 dictonary.")
	#Yes, 'model' is one of the keys in the thisdict1 dictonary.

#Change Dictionary Items : 

#Change values : You can change the value of a specific item by referring to its key name :

print("\nChange the 'year' to 2018 : \n")
thisdict1["year"] = 2018
print(thisdict1) #{'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

#Update dictonary : Will update the dictonary with the items from the given argument.
#The argument must be a dictonary, or an iterable object with key:value pairs.

print("\nUpdate the 'year' of the car by using the update() method : \n")

print("\nBefore Update : \n")
print(thisdict1) #{'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

print("\nAfter Update : \n")
thisdict1.update({"year" : 2020}) 
print(thisdict1) #{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

#Adding Items : Adding an item to the dictonary is done by using a new index key and assigning a value to it :

print("\nBefore Update : \n")
print(thisdict1) #{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

print("\nAfter Update : \n")
thisdict1["color"] = "red"
print(thisdict1) #{'brand': 'Ford', 'model': 'Mustang', 'year': 2020, 'color': 'red'}

#Update dictonary : 

'''
	-The update() method will update the dictionary with the items from a given argument. If the item does not exist, 
	the item will be added.
	- The argument must be a dictionary, or an iterable object with key:value pairs.
'''

print("\nBefore Update : \n")
print(thisdict1) #{'brand': 'Ford', 'model': 'Mustang', 'year': 2020, 'color': 'red'}

print("\nAfter Update : \n")
thisdict1.update({"color" : "blue"})
print(thisdict1) #{'brand': 'Ford', 'model': 'Mustang', 'year': 2020, 'color': 'blue'}

#Remove Dictonary : 

#Removing Items : There are several methods to remove items from a dictonary : 

#The pop() method removes the item with the specified key name : 

print("\nBefore Update : \n")
print(thisdict1)	#{'brand': 'Ford', 'model': 'Mustang', 'year': 2020, 'color': 'blue'}

print("\nAfter Update : \n")
thisdict1.pop("model")
print(thisdict1)	#{'brand': 'Ford', 'year': 2020, 'color': 'blue'}

print("\nThe popitem() method removes the last inserted item :\n")

print("\nBefore removes : \n")
print(thisdict1)	#{'brand': 'Ford', 'year': 2020, 'color': 'blue'}

print("\nAfter removes : \n")
thisdict1.popitem()
print(thisdict1)	#{'brand': 'Ford', 'year': 2020}

print("\nThe del keyword removes the item with the specified key name : \n")
print("\nBefore delelte : \n")
print(thisdict2)

print("\nAfter delelte : \n")
# del thisdict2	
print(thisdict2) #this will cause an error because "thisdict" no longer exists.

print("\nBefore clear : \n")
print(thisdict3) #{'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}

print("\nAfter clear : \n")
thisdict3.clear()
print(thisdict3) #{}

#Loop Through a Dictonary : You can loop through a dictonary using for loop.

'''
	- When looping through a dictonary, the return value are the kays of the dictonary, but there are methods to return the values as well: 
'''

thisdict1 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print("\nPrint all key names in the dictonary, one by one : \n")

for x in thisdict1:
	print(x) 

'''
	brand
	model
	year
'''

print("\nPrint all values in the dictonary, one by one : \n")

for x in thisdict1:
	print(thisdict1[x])

'''
	Ford
	Mustang
	1964
'''

print("\nYou can also use the values() method to return values of a dictionary :\n")

for x in thisdict1.values():
	print(x)

'''
	Ford
	Mustang
	1964
'''

print("\nYou can use the keys() method to return the keys of a dictionary :\n")

for x in thisdict1.keys():
	print(x)

'''
	brand
	model
	year
'''

print("\nLoop through both keys and values, by using the items() method :\n")

for x, y in thisdict1.items():
	print(x ,' : ', y)

'''
	brand  :  Ford
	model  :  Mustang
	year  :  1964
'''

#Copy a Dictonary : 

'''
	- You can't copy a dictonary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made 
	in dict1 will automatically also be made in dict2.
	- There are ways to make a copy, one way is to use the built-in Dictonary method copy().
'''

print("\nMake a copy of a dictionary with the copy() method : \n")

thisdict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

mydict = thisdict1.copy()
print(mydict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#Another way to make a copy is to use the built-in function dict().

print("\nMake a copy of a dictonary with the dict() function : \n")

mydict = dict(thisdict1)
print(mydict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#Nested Dictonaries : 

print("\nCreate a dictonary that contain three dictonaries : \n")

myfamily = {
	"child1" : {
	"name" : "Emil",
	"year" : 2004
	},

	"child2" : {
	"name" : "Tobias",
	"year" : 2007
	},

	"child3" : {
	"name" : "Linus",
	"year" : 2011
	}
}

print(myfamily) #{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

#Or, if you want to add three dictionaries into a new dictionary:

print("\nCreate three dictionaries, then create one dictionary that will contain the other three dictionaries :\n")

child1 = {
	"name" : "Emil",
	"year" : 2004
}

child2 = {
	"name" : "Tobias",
	"year" : 2007
}

child3 = {
	"name" : "Linus",
	"year" : 2011
}

myfamily = {
	"child1" : child1,
	"child2" : child2,
	"child3" : child3
}

print(myfamily) #{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

#Access items in nested dictonaries : 

'''
	- To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:
'''

print("\nPrint the name of child 2 : \n")

print(myfamily["child2"] ["name"]) #Tobias

#Loop Through nested dictonaries :

for x, obj in myfamily.items():
	print(x)

	for y in obj:
		print(y + ':', obj[y])

'''
	child1
	name: Emil
	year: 2004

	child2
	name: Tobias
	year: 2007

	child3
	name: Linus
	year: 2011
'''

'''
	- Dictionary Methods : Python has a set of built-in methods that you can use on dictionaries.

	Method									Description
	clear()					Removes all the elements from the dictionary
	copy()					Returns a copy of the dictionary
	fromkeys()			Returns a dictionary with the specified keys and value
	get()						Returns the value of the specified key
	items()					Returns a list containing a tuple for each key value pair
	keys()					Returns a list containing the dictionary's keys
	pop()						Removes the element with the specified key
	popitem()				Removes the last inserted key-value pair
	setdefault()		Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
	update()				Updates the dictionary with the specified key-value pairs
	values()				Returns a list of all the values in the dictionary
'''