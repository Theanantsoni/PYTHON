#python list.py

#List : 

'''Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets: '''

print("\n#List :\n")

thislist = ["apple", "banana", "cherry"]
print(thislist)

#List Duplicate Allow

print("\n#List Duplicate Allow\n")

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

'''
	List Items : List items are ordered, changeable, and allow duplicate values.
	List items are indexed, the first item has index [0], the second item has index [1] etc.

	Ordered : When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
	If you add new items to a list, the new items will be placed at the end of the list.

	Note: There are some list methods that will change the order, but in general: the order of the items will not change.

	Changeable
	The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

	Allow Duplicates
	Since lists are indexed, lists can have items with the same value:
'''

#List Length

print("\n#List Length\n")

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#List Items - Data Types

print("\n#List Items - Data Types\n")

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

#list with strings, integers and boolean values

print("\n#list with strings, integers and boolean values\n")

list1 = ["abc", 34, True, 40, "male"]
print(list1)

#List type ... <class 'list'>

print("\n#List type ... <class 'list'>\n")

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#list() Constructor

print("\n#list() Constructor\n")

thislist = list(("apple", "banana", "cherry"))
print(thislist)

'''
	Python Collections (Arrays) : 
	There are four collection data types in the Python programming language:

	List : 
	is a collection which is ordered and changeable. Allows duplicate members.
	Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
	
	Set :
	is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
	
	Dictionary :
	is a collection which is ordered** and changeable. No duplicate members.
	*Set items are unchangeable, but you can remove and/or add items whenever you like.

	When choosing a collection type, it is useful to understand the properties of that type. 
	Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.
'''

# -----------------------------------------------------------------------------

thislist1 = ["apple",'banana','cherry','orange','kiwi','melon','mango']

#Access Items :

print("\n#Access Items :\n")

print(thislist1[1])

#Negative Indexing :

print("\n#Negative Indexing :\n")

print(thislist1[-1])

'''
	Range of Indexes :	You can specify a range of indexes by specifying where to start and where to end the range.
	When specifying a range, the return value will be a new list with the specified items.
'''

#Range of Indexes :

print("\n#Range of Indexes :\n")

print(thislist1[2:5])

#Find starting values :

print("\n#Find starting values :\n")

print(thislist1[:4])

#Find Ending values :

print("\n#Find Ending values :\n")

print(thislist1[2:])

#Range of Negative Indexes :

print("\n#Range of Negative Indexes :\n")

print(thislist1[-4:-1])

#Check if Item Exists :

print("\n#Check if Item Exists :\n")

if "apple" in thislist1:
	print("Yes, 'apple' in thislist")

# -----------------------------------------------------------------------------

thislist2 = ["apple",'banana','cherry','orange','kiwi','melon','mango']

#Change item value :

print("\n#Change item value :\n")

thislist2[1] = "blackcurrent"
print(thislist2)

''' 
	Change a Range of Item Values : To change the value of items within a specific range, 
	define a list with the new values, and refer to the range of index numbers where you want to insert the new values:
'''

#Change a Range of Item values :

print("\n#Change a Range of Item values :\n")

thislist2[0] = ["whitecurrant", "watermelon"]
print(thislist2)

thislist2[1:3] = ["White","black"]
print(thislist2)

# -----------------------------------------------------------------------------

thislist3 = ["apple",'banana','cherry','orange','kiwi','melon','mango']
thislist4 = ["White","Black","Red","Blue","Purple"]

thislist5 = ["White","Black","Red"]
thislist6 = ["Banana","Orange","Lemon"]

#Insert Items in List :

print("\n#Insert Items in List :\n")

thislist3.insert(2,"watermelon")
print(thislist3)

#Append Items in List :	Add item in last index

print("\n#Append Items in List :	Add item in last index\n")

thislist3.append("white")
print(thislist3)

#Extend List : Combine both items in one list

print("\n#Extend List : Combine both items in one list\n")

thislist3.extend(thislist4)
print(thislist3)

#Add any Iterable :

print("\n#Add any Iterable :\n")

thislist5.extend(thislist6)
print(thislist5)

# -----------------------------------------------------------------------------

#Remove List Items : 

print("\n#Remove List Items : \n")

thislist7 = ["apple","banana","mango","orange","lemon"]
thislist8 = ["white","black","red","purple","yellow"]
thislist9 = ["white","black","red","purple","yellow"]

#Remove Specified Item :

thislist7.remove("banana")
print(thislist7)

#Remove specified Index :

print("\n#Remove Specified Item :\n")

thislist8.pop(1)	#Remove banana Index
thislist8.pop()		#Remove Last Index

#del Keyword also removes the specified index:

print("\n#del Keyword also removes the specified index:\n")

del thislist[0]	#Remvoe 0 Index
del thislist8 #this will cause an error because you have succsesfully deleted "thislist".

#Clear the List

print("\n#Clear the List\n")

thislist9.clear()
print(thislist9)	#Clear all data in List Print only "[]".

# -----------------------------------------------------------------------------

#Loop Lists :

print("\n#Loop Lists :\n")

#Loop Through a List :

print("\n#Loop Through a List :\n")

list1 = ["apple","banana","cherry"] 

#Using the For Loop :

print("\n#Using the For Loop :\n")

for x in list1:
	print(x)

#Loop Through the Index Numbers :

print("\n#Loop Through the Index Numbers :\n")

for i in range(len(list1)):
	print(list1[i])

#Using the While Loop :

print("\n#Using the While Loop :\n")

i = 0
while i < len(list1):
	print(list1[i])
	i = i+1

'''

List Comprehension :

List comprehension offers a shorter syntax when you want to 
create a new list based on the values of an existing list.

Example:

Based on a list of fruits, you want a new list, containing only 
the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement 
with a conditional test inside:

'''

#Looping Using List Comprehension :

print("\n#Looping Using List Comprehension :\n")

list2 = ["apple","banana","cherry","kiwi","mango"]
newlist = []

[print(x) for x in list2]

#First Method :

print("\n#First Method :\n")

for x in list2:
	if "a" in x:	# if the character "a" is present in x.
		newlist.append(x)	
print(newlist)

#Second Method :

print("\n#Second Method :\n")

newlist = [x for x in list2 if "a" in x]
print(newlist)

# -----------------------------------------------------------------------------

#The Syntax :

# newlist = [expression for item in iterable if condition == true]

#Condition : 

print("\n#Condition : \n")

newlist = [x for x in list2 if x != "apple"]
print(newlist)

#Iterable :

print("\n#Iterable :\n")

newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

#Expression : 

print("\n#Expression : \n")

list3 = ["apple","banana","cherry","kiwi","mango"]

newlist = [x.upper() for x in list3] #All Value in UpperCase..
print(newlist)

newlist = ['hello' for x in list2]	#Set All value in new list to 'hello'..
print(newlist)

newlist = [x if x!= "banana" else "orange" for x in list3] #replaces "banana" with "orange"
print(newlist)

# -----------------------------------------------------------------------------

#Sort Lists : List objects have a sort() method that will sort the list alphanumerically, ascending.

#Sort the list alphanumerically :

print("\n#Sort the list alphanumerically :\n")

thislist1 = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#Sort the list Numerically :

print("\n#Sort the list Numerically :\n")

thislist2 = [100,50,65,82,23]
thislist.sort()
print(thislist)

#Sort Descending :

print("\nSort Descending : \n")

#First Method :

print("\nFirst Method : \n")

thislist1.sort(reverse = True)
print(thislist1)

thislist2.sort(reverse = True)
print(thislist2)

#Second Method :

print("\nSecond Method : \n")

print(sorted(thislist1, reverse=True))

print(sorted(thislist2, reverse=True))

#Sort Ascending :

print("\nSort Ascending : \n")

#First Method :

print("\nFirst Method : \n")

thislist1.sort()
print(thislist1)

thislist2.sort()
print(thislist2)

#Second Method :

print("\nSecond Method : \n")

print(sorted(thislist1))

print(sorted(thislist2))

#Customize Sort Function : 

print("\n#Customize Sort Function : \n")

'''You can also customize your own function by using the 
keyword argument key = function.

#The function will return a number that will be used to 
sort the list. (The lowest number first) '''

#Sort the list based on how close the number is to 50 :

print("\n#Sort the list based on how close the number is to 50 :\n")

def myfunc(n):
	return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#Case Insensitive Sort :

print("\n#Case Insensitive Sort :\n")

#Case sensitive sorting can give an unexpected result:

print("\nCase sensitive sorting can give an unexpected result :\n")

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

''' Luckily we can use built-in functions as key functions when sorting a list.
So if you want a case-insensitive sort function, use str.lower as a key function: '''

#Perform a case-insensitive sort of the list :

print("\nPerform a case-insensitive sort of the list : \n")

thislist.sort(key = str.lower)
print(thislist)

#Reverse Order : The reverse() method reverses the current sorting order of the elements.

#Reverse the order of the list items :

print("\n#Reverse the order of the list items :\n")

thislist.reverse()
print(thislist)

#Copy a List :

'''You cannot copy a list simply by typing list2 = list1, because: list2 will only be a 
reference to list1, and changes made in list1 will automatically also be made in list2.'''

#Use the copy() method :

print("\n#Use the copy() method :\n")

#Make a copy of a list with the copy() method : 

print("\n#Make a copy of a list with the copy() method : \n")

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Use the list() method :

print("\n#Use the list() method :\n")

mylist = list(thislist)
print(mylist)

#Use the Slice Operator :

print("\n#Use the Slice Operator : \n")

mylist = thislist[:]
print(mylist)

#Join Lists :

#Join Two Lists : There are several ways to join, or concatenate, two or more lists in python
#One of the easiest ways are by using the + operator.
#Or you can use the extend() method, where the purpose is to add elements from one list to another list.

#Join two lists :

print("\n#Join two lists :\n")

list1 = ['a','b','c']
list2 = [1,2,3]

list3 = list1 + list2
print(list3)

#Append list2 into list1 :

print("\n#Append list2 into list1 :\n")

for x in list2:
	list1.append(x)
print(list1)

#Use the extend() method to add list2 at the end of list1

print("\n#Use the extend() method to add list2 at the end of list1 : \n")

list1.extend(list2)
print(list1)

#List Methods : 

#Python has a set of built-in methods that you can use on lists.

'''

Methods					Description

append()	Adds an element at the end of the list
clear()		Removes all the elements from the list
copy()		Returns a copy of the list
count()		Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()		Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()		Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()		Sorts the list

'''