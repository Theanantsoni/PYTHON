#python set.py

'''
	Set : Sets are used to store multiple items in a single variable.
	- Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
	- A set is a collection which is unordered, unchangeable*, and unindexed.
	* Note: Set items are unchangeable, but you can remove items and add new items.
	Sets are written with curly brackets.

'''
myset = {'apple', 'banana', 'cherry'}
print(myset)	#{'cherry', 'banana', 'apple'}

#Set items : Set items are unordered, unchangeable, and do not allow duplicate values.
#Unordered : Means that the items in a set do not have a defined order.
#Unchangeable : Means that we cannot change the items after the set has been created.

#Once a set is created, you can't change its items, but you can remove items and add new items.
#Duplicates Not Allowed : Set can't have two items with the same value.

print("\nDuplicate values will be ignored:\n")
thisset = {'apple', 'banana', 'cherry', 'apple'}
print(thisset)	#{'banana', 'cherry', 'apple'}

#Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:

print("\nTrue and 1 is considered the same value:\n")
thisset = {'apple', 'banana', 'cherry', True, 1, 2}
print(thisset)	#{True, 2, 'banana', 'cherry', 'apple'}

#Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:

print("\nFalse and 0 is considered the same value:\n")
thisset = {'apple', 'banana', 'cherry', False, True, 0}
print(thisset)	#{False, True, 'cherry', 'apple', 'banana'}

#Get the Length of a Set : To determine how many items a set has, use the len() function.

print("\nGet the number of items in a set : \n")
print(myset)	#3

#Set Items- Data Types : 

print("\nString, int and boolean data types :\n")
set1 = {'apple', 'banana', 'cherry'}	#{'cherry', 'apple', 'banana'}
set2 = {1, 5, 7, 9, 3}	#{1, 3, 5, 7, 9}
set3 = {True, False, False}	#{False, True}

print("\nA set with strings, integers and boolean values :\n")
set1 = {'abc', 34, True, 40, 'male'}	#{True, 34, 40, 'male', 'abc'}

#Type() : From python's perspective, sets are defined as objects with the data type 'set':
#<class 'set'>

print(type(set1))	#<class 'set'>

#Set() Constructor : It is also possible to use the set() constructor to make a set.

print("\nUsing the set() constructor to make a set :\n") 
thisset = set(('apple', 'banana', 'cherry')) # note the double round-brackets
print(thisset)	#{'banana', 'apple', 'cherry'}

'''
	Python Collections (Arrays): There are four collection data types in the Python programming language:

	List : is a collection which is ordered and changeable. Allows duplicate members.
	Tuple : is a collection which is ordered and unchangeable. Allows duplicate members.
	Set : is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
	Dictionary : is a collection which is ordered** and changeable. No duplicate members.
	
	*Set items are unchangeable, but you can remove items and add new items.

	When choosing a collection type, it is useful to understand the properties of that type. 
	Choosing the right type for a particular data set could mean retention of meaning, and, it 
	could mean an increase in efficiency or security.
'''

#Access Set Items : You can't access items in a set by referring to an index or a key.

'''
	But you can loop through the set items using a for loop, or ask if a specified value is present in a set, 
	by using the in keyword.
'''

print("\nLoop through the set, and print the values :\n")
for x in thisset:
	print(x)

''' apple
banana
cherry '''

print("\nCheck if 'banana' is present in the set :\n")
thisset = {'apple', 'banana', 'cherry'}
print("banana" in thisset) #True

print("\nCheck if 'banana' is NOT present in the set : \n")
print("banana" not in thisset)	#False

#Change items : Once a set is created, you can't change its items, but you can add new items.

#Add Set Items : 

#Add Items: Once a set is created, You can't change its items, but you can add new items.
#To add one items to a set use the add() method.

print("\nAdd an item to a set, using the add() method : \n")
thisset.add("orange")
print(thisset)	#{'apple', 'banana', 'cherry', 'orange'}

#Add Sets : To add items from another set into the current set, use the update() method.

print("\nAdd elements from tropical into thisset : \n")

thisset = {'apple', 'banana', 'cherry'}
tropical = {'pineapple', 'mango', 'papaya'}
thisset.update(tropical)
print(thisset)	#{'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}

#Add any Iterable : 

'''
	The object in the update() method does not have to be a set, 
	it can be any iterable object (tuples, lists, dictonaries).
'''

#Remove Set Items : 
#Remove Items : To remove an item in a set, use the remove(), or the discard() method.

print("\nRemove 'banana' by using the remove() method :\n")
thisset = {'apple', 'banana', 'cherry'}
thisset.remove("banana")
print(thisset)	#{'cherry', 'apple'}

#Note: If the item to remove does not exist, remove() will raise an error.

print("\nRemove 'banana' by using the discard() mrthod : \n")
thisset = {'apple', 'banana', 'cherry'}
thisset.discard("banana")
print(thisset) #{'apple', 'cherry'}

#Note: If the item to remove does not exist, discard() will NOT raise an error.

'''
	- You can also use the pop() method to remove an item, but this method will remove a 
	random item, so you cannot be sure what item that gets removed.
	- The return value of the pop() method is the removed item.
'''

print("\nRemove a random item by using the pop() method :\n")
thisset = {'apple', 'banana', 'cherry'}
x = thisset.pop()
print(x)	#apple
print(thisset)	#{'banana', 'cherry'}

#Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

print("\nThe clear() method empties the set :\n")
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) #set()

#The del keyword will delete the set completely :
thisset = {"apple", "banana", "cherry"}
# del thisset
print(thisset)	#this will raise an error because the set no longer exists

#Loop Sets : 
#Loop Items : You can loop through the set items by using a for loop.

print("\nLoop through the set, and print the values.\n")
for x in thisset:
	print(x)

'''
	apple
	cherry
	banana
'''

#Join Sets : There are several ways to join two or more sets in python.

'''
	- The union() and update() methods joins all items from both sets.
	- The intersection() method keeps ONLY the duplicates.
	- The difference() method keeps the items from the first set that are not in the other set(s).
	- The symmetric_difference() method keeps all items EXCEPT the duplicates.
'''

#Union : Returns a new set with all items from both sets.

print("\nJoin set1 and set2 into a new set : \n")
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)	#{'c', 3, 2, 'a', 'b', 1}

#You can use the | operator instead of the union() method, and you will get the same result.

print("\nUse | to join two sets : \n")
set3 = set1 | set2
print(set3)	#{'b', 'c', 1, 3, 2, 'a'}

#Join Multiple Sets : 

'''
	- All the joining methods and operators can be used to join multiple sets.
	- When using a method, just add more sets in the parentheses, separated by commas:
'''

print("\nJoin multiple sets with the union() method : \n")
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
set3 = {'John', 'Elena'}
set4 = {'apple', 'bananas', 'cherry'}

myset = set.union(set2, set3, set4)
print(myset) #{cherry, banana, 2, 3, apple, 1, 'b', John, 'c', Elena, 'a'}

#When using the | operator, seperate the sets with more | operators:

print("\nUse | to join sets :\n")
myset = set1 | set2 | set3 | set4
print(myset)	#{John, 'b', banana, 3, 2, apple, Elena, 'a', 'c', 1, cherry}

#Join a Set and Tuple : 

'''
	The union() method allows you to join a set with other data types, like lists or tuples.
	The result will be a set.
'''

print("\nJoin a set with a tuple : \n")
x = {"a", "b", "c"}
y = {1, 2, 3}
z = x.union(y)
print(z)	#{1, 'b', 2, 'c', 3, 'a'}

'''
	Note: The  | operator only allows you to join sets with sets, and not with other data types 
	like you can with the  union() method.
'''

#Update : 

#The update() method inserts all items from one set into another.
#The update() changes the original set, and does not return a new set.

print("\nThe update() method inserts the items in set2 into set1 :\n")

x.update(y)
print(x) #{3, 1, 'b', 'c', 2, 'a'}

#Intersection : Keep ONLY the duplicates.

#The Intersection() method will return a new set, that only contains the items that are present in both sets.

print("\nJoin Set1 and Set2, but keep only the duplicates :\n")
set1 = {'apple', 'banana', 'cherry'}
set2 = {'google', 'microsoft', 'apple'}

set3 = set1.intersection(set2)
print(set3) #{'apple'}

#You can use the & operator instead of the intersection() method, and you will get the same result.

print("\nUse & to join sets :\n")
set3 = set1 & set2
print(set3)	#{'apple'}

'''
	Note: The & operator only allows you to join sets with sets, and not with other data types like you 
	can with the intersection() method.
	- The intersection_update() method will also keep ONLY the duplicates, but it will change the original 
	set instead of returning a new set.
'''

print("\n\nKeep the items that exists in both set1, and set2 :")

set.intersection_update(set2)
print(set1) #{'apple'}

#The values True and 1 are considered the same value, The same goes for False and 0.

print("\nJoin sets that contains the values True, False, 1 and 0, and see what is considered as duplicates :\n")

set1 = {'apple', 1, 'banana', 0, 'cherry'}
set2 = {False, 'google', 1, 'apple', 2, True}
set3 = set1. intersection(set2)
print(set3) #{False, True, 'apple'}

#Difference : 

'''
	difference() Method : return a new set that will contain only the items from the first set that are not present 
	in the other set.
'''

print("\nKeep all items from set1 that are not in set2 :\n")
set1 = {'apple', 'banana', 'cherry'}
set2 = {'google', 'microsoft', 'apple'}

set3 = set1.difference(set2)
print(set3) #{'banana', 'cherry'}

#You can use the - operator instead of the difference() method, and you will get the same result.

print("\nUse - to join two sets :\n")
set3 = set1 - set2
print(set3) #{'banana', 'cherry'}

'''
	Note: The - operator only allows you to join sets with sets, and not with other data types like you can with 
	the difference() method.
'''

print("\nUse the difference_update() method to keep the items that are not present in both sets :\n")

set1.difference_update(set2)
print(set1) #{'banana', 'cherry'}

#Symmetric Differences : method will keep only the elements that are NOT present in both sets.

print("\nKeep the items that are not present in both sets : \n")

set3 = set1.symmetric_difference(set2)
print(set3)	#{'google', 'banana', 'microsoft', 'cherry'}

#You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.

print("\nUse ^ to join two sets : \n")
set3 = set1 ^ set2
print(set3)	#{'google', 'banana', 'microsoft', 'cherry'}

'''
	Note: The ^ operator only allows you to join sets with sets, and not with other data types like you can 
	with the symmetric_difference() method.
'''

print("\nUse the symmetric_difference_update() method to keep the items that are not present in both sets :\n")

set1.symmetric_difference_update(set2)
print(set1)	#{'google', 'banana', 'microsoft', 'cherry'}

#Set Methods :

'''
	Method						Shortcut						Description
	add()	 												Adds an element to the set
	clear()	 												Removes all the elements from the set
	copy()	 												Returns a copy of the set
	difference()					-						Returns a set containing the difference between two or more sets
	difference_update()				-=						Removes the items in this set that are also included in another, specified set
	discard()	 											Remove the specified item
	intersection()					&						Returns a set, that is the intersection of two other sets
	intersection_update()			&=						Removes the items in this set that are not present in other, specified set(s)
	isdisjoint()	 										Returns whether two sets have a intersection or not
	issubset()						<=						Returns whether another set contains this set or not
	 								<						Returns whether all items in this set is present in other, specified set(s)
	issuperset()					>=						Returns whether this set contains another set or not
	 								>						Returns whether all items in other, specified set(s) is present in this set
	pop()	 												Removes an element from the set
	remove()	 											Removes the specified element
	symmetric_difference()			^						Returns a set with the symmetric differences of two sets
	symmetric_difference_update()	^=						Inserts the symmetric differences from this set and another
	union()							|						Return a set containing the union of sets
	update()						|=						Update the set with the union of this set and others
'''









