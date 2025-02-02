#python tuple.py

#tuple : 

'''
	Tuples are used to store multiple items in a single variable.
	Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, 
	all with different qualities and usage.
	A tuple is a collection which is ordered and unchangeable.
	Tuples are written with round brackets. 
'''

mytuple = ("apple", "banana", "cherry")
print(mytuple)

'''
	Tuple Items :
	Tuple items are ordered, unchangeable, and allow duplicate values.
	Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

	Ordered :
	When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

	Unchangeable :
	Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

	Allow Duplicates :
	Since tuples are indexed, they can have items with the same value: 
'''

# -----------------------------------------------------------------------------

print("\n#Allow Duplicates :\n")

thistuple = ("apple", "banana", "cherry", "apple", "apple", "cherry")
print(thistuple)

print("\n#Create Tuple With One Item : \n")

''' 
	To create a tuple with only one item, You have to add a comma after the item, otherwise python will be 
	not recognize it as a tuple

'''
#One item tuple, remember the comma:

print("\n#One item tuple, remember the comma:\n")

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple

print("\n#NOT a tuple\n")

thistuple = ("apple")
print(type(thistuple))

#Tuple Items - Data Types : 

#Tuple items can be any data types :

#String, int and boolean data types :

print("\n#Tuple Items - Data Types : \n")

print("\n#String, int and boolean data types :\n")

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

#A tuple can contain different data types :

#A tuple with strings, integers and boolean values :

print("\n#A tuple with strings, integers and boolean values :\n")

#type() : From Python's perspective, tuples are defined as objects with the data type 'tuple' :
#<class 'tuple'>

print(type(tuple1))

#The tuple() Constructor : It is also possible to use tuple() constructor to make a tuple.

#Using the tuple() method to make a tuple :

print("\n#Using the tuple() method to make a tuple :\n")

thistuple = tuple(("apple", "banana", "cherry")) #note the double round-brackets
print(thistuple)

#Python Collections (Arrays) : There are four collection data types in the python programming language:

''' 
	List is a collection which is ordered and changeable. Allows duplicate members.
	Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
	Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
	Dictionary is a collection which is ordered** and changeable. No duplicate members. 

	Set items are unchangeable, but you can remove and/or add items whenever you like.

	When choosing a collection type, it is useful to understand the properties of that type. Choosing the right 
	type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency 
	or security.
'''

#Access Tuple Items : You can access tuple items by referring to the index number, inside square brackets:

#Print the second item in the tuple :

# -----------------------------------------------------------------------------

print("\n\nAccess Tuple Items : ")

print("\n#Print the second item in the tuple :\n")

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Negative Indexing : 

''' 
	Negative indexing means start from the end.
	-1 refers to the last item, -2 refers to the second last item etc
'''

# -----------------------------------------------------------------------------

#Range of Indexes :

'''
	You can specify a range of indexes by specifying where to start and where to end the range.
	When specifying a range, the return value will be a new tuple with the specified items.
'''

#Return the third, fourth, and fifth items : 

print("\n#Return the third, fourth, and fifth items : \n")

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

'''
	Note: The search will start at index 2 (included) and end at index 5 (not included).
	Remember that the first item has index 0.
'''

#By leaving out the start value, the range will start at the first item:

#This example returns the items from the beginning to, but NOT included, "kiwi".

print("\n#This example returns the items from the beginning to, but NOT included, 'kiwi'.\n")

print(thistuple[:4])

#By leaving out the end value, the renge will go on to the end of the tuple:

#This example returns the items from "cherry" and to the end :

print("\n#This example returns the items from 'cherry' and to the end :\n")

print(thistuple[2:])

#Range of Negative Indexes : Specify negative indexes if you want to start the search from the end of the tuple:

#This example returns the items from index -4 (included) to index -1 (excluded)

print("\n#This example returns the items from index -4 (included) to index -1 (excluded)\n")

print(thistuple[-4 : -1])

#Check if item Exists : To determine if a specified item is present in a tuple use the in keyword:

#Check if the "apple" is present in the tuple :

print("\n#Check if the 'apple' is present in the tuple :\n")

if "apple" in thistuple :
	print("Yes, 'apple' is in the fruits tuple." )

# -----------------------------------------------------------------------------

#Update Tuples :

'''
	Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
	But there are some workarounds.

	Change Tuple Values :
	Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
	But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
'''

print("\n#Update Tuples :\n")

#Convert the tuple into a list to be able to change it :

print("\n#Convert the tuple into a list to be able to change it :\n")

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# -----------------------------------------------------------------------------

#Add Items :

print("\n#Add Items : \n")

'''
	Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.

	1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and 
	convert it back into a tuple.
'''

#Convert the tuple into a list :

print("\n#Convert the tuple into a list : \n")

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

'''
		2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), 
		create a new tuple with the item(s), and add it to the existing tuple:
'''

#Create a new tuple with the value "orange", and add that tuple :

print("\n#Create a new tuple with the value 'orange', and add that tuple :\n")

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

'''
	Note: When creating a tuple with only one item, remember to include a comma after the item, 
	otherwise it will not be identified as a tuple.
'''

#Remove Items : You cannot remove items in a tuple.
'''
	Tuple are unchangeable, So you cannot remove items from it, but you can use the same workaround
	as we used for changing and adding tuple items:
'''

#Convert the tuple into a list, remove 'apple', and convert it back into a tuple:

print("\n#Convert the tuple into a list, remove 'apple', and convert it back into a tuple:\n")

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#Or you can delete the tuple completely:

#The del keyword can delete the tuple completely:

print("\n#The del keyword can delete the tuple completely:\n")

thistuple = ("apple", "banana", "cherry")
del thistuple

#print(thistuple) #This will raise an error because the tuple no longer exists

# -----------------------------------------------------------------------------

#Unpack Tuples : 

'''
	When we create a tuple, We normally assign values to it. 
	This is calles "Packing" a Tuple.
'''

print("\n#Unpack Tuples :\n")
print("\nPacking a Tuple : \n")

tuple1 = ("apple", "banana", "cherry")
print(tuple1)

'''
	But, in python, we are also allowed to extract the values back into variables.
	This is called "Unpacking".
'''

print("\nUnpacking a tuple : \n")

tuple1 = ("apple", "banana", "cherry")

(green, yellow, red) = tuple1

print(green)	#apple
print(yellow)	#banana
print(red)		#cherry

'''
	Note : he number of variables must match the number of values in the tuple, 
	if not, you must use an asterisk to collect the remaining values as a list.
'''

# -----------------------------------------------------------------------------

#Using Asterisk*

print("\n#Using Asterisk*\n")

#Assign the rest of the values as a list called "red".

print("\n#Assign the rest of the values as a list called 'red'.\n")

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, white, *red) = fruits

print(green)	#apple
print(yellow)	#banana
print(white)	#cherry
print(red)		#['strawberry', 'raspberry']

'''
	If the asterisk is added to another variable name than the last, python will
	assign values to the variable until the number of values left matches the 
	number of variables left.
'''

# -----------------------------------------------------------------------------

#Add a list of values the "tropic variable"

print("\n#Add a list of values the 'tropic variable'\n")

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)	#apple
print(tropic)	#mango
print(red)		#['mango', 'papaya', 'pineapple']

# -----------------------------------------------------------------------------

#Python - Loop Tuples : You can loop through the tuple items by using a for loop.

print("\n#Python - Loop Tuples :\n")

#Iterate through the items and print the values :

print("\n#Iterate through the items and print the values :\n")

thistuples = ("apple", "banana", "cherry")
for x in thistuples:
	print(x)

#Loop Through the index numbers :

'''
	You can also the tuple items by referring to their index number.
	Use the range() and len() functions to create a suitable iterable.
'''

#Print all items by referring to index number :

print("\n#Print all items by referring to index number :\n")

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
	print(thistuple[i])

# -----------------------------------------------------------------------------

#Using a While Loop :

'''
	You can loop through the tuple items by using a while loop.
	Use the len() function to determine the length of the tuple, 
	then start at 0 and loop your way through the tuple items by referring to their indexes.
	Remember to increase the index by 1 after each iteration.
'''

#Print all items, using a while loop to go through all the index numbers :

print("\n#Print all items, using a while loop to go through all the index numbers :\n")

thisyuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
	print(thistuple[i])
	i = i + 1

# -----------------------------------------------------------------------------

#Join Two Tuples : Use the + Operator.

#Join two Tuples : 

print("\n#Join two Tuples : \n")

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# -----------------------------------------------------------------------------

#Multiply Tuples : Use the * Operator.

print("\n#Multiply Tuples :\n")

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

# -----------------------------------------------------------------------------

#Tuple Methods : Python has two Built-in Methods : 

'''
	count()	:
	Returns the number of times a specified value occurs in a tuple
	
	index()	:
	Searches the tuple for a specified value and returns the position of where it was found
'''
