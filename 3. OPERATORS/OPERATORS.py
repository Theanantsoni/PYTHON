# python OPERATORS.py

#----------------------------------------- Arithmetic Operators ------------------------------------------

a = 5
b = 10

print("\nARITHMETIC OPERATORS...")

print("Addition of A+B is : ",a+b)
print("Subtraction of B-A is : ",b-a)
print("Multiplication of A*B is : ",a*b)
print("Division of B/A is : ",b/a)
print("Modules of A'%'B is :", a%b)
print("Exponentiation of A**B is : ", a**b)
print("Floor division of A//B is : ", a//b)

#----------------------------------------- Assignment Operators ------------------------------------------

print("\nASSIGNMENT OPERATORS...")

x = 10
print("x = 10")

x += 2
print("x += 2  ->", x)

x -= 2
print("x -= 2  ->", x)

x *= 2
print("x *= 2  ->", x)

x /= 2
print("x /= 2  ->", x)

x %= 3
print("x %= 3  ->", x)

x = 10  # Reset x
x //= 3
print("x //= 3 ->", x)

x = 10  # Reset x
x **= 3
print("x **= 3 ->", x)

x = 10  # Reset x
x &= 3
print("x &= 3  ->", x)

x = 10  # Reset x
x |= 3
print("x |= 3  ->", x)

x = 10  # Reset x
x ^= 3
print("x ^= 3  ->", x)

x = 10  # Reset x
x >>= 2
print("x >>= 2 ->", x)

x = 10  # Reset x
x <<= 2
print("x <<= 2 ->", x)

print("\nWALRUS OPERATOR...")  # := operator (Walrus operator)
print(x := 3)  # Assigns 3 to x and prints it

#----------------------------------------- Comparision Operator ------------------------------------------

print("\nCOMPARISON OPERATORS...")

x = 5
y = 1

print("x = 5, y = 1")

a = (x < y)
print("5 < 1  ->", a)

b = (x > y)
print("5 > 1  ->", b)

c = (x <= y)
print("5 <= 1 ->", c)

d = (x >= y)
print("5 >= 1 ->", d)

e = (x == y)
print("5 == 1 ->", e)

f = (x != y)
print("5 != 1 ->", f)

#----------------------------------------- LOGICAL OPERATORS ------------------------------------------

print("\nLOGICAL OPERATORS...")

a=True
b=False

#AND operator...

print("The value of A and B is : ",(a and b)) #Returns True if both statements are true...
x = 5
print(x > 3 and x < 10)

#OR operator...

print("The value of A or B is : ",(a or b))   #Returns True if one of the statements is true...
x = 5
print(x > 3 or x < 4)

#NOT operator...

print("The value of not b is : ",(not b))     #Reverse the result,returns False if the result is true...
x = 5
print(not(x > 3 and x < 10))

#----------------------------------------- Identity Operators ------------------------------------------

#in operator...

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # returns True because z is the same object as x

print(x is y) # returns False because x is not the same object as y, even if they have the same content

print(x == y) # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

#not in operator...

x = ["apple", "banana"]

print("pineapple" not in x) # returns True because a sequence with the value "pineapple" is not in the list


'''
ARITHMETIC OPERATORS...
Addition of A+B is :  15
Subtraction of B-A is :  5
Multiplication of A*B is :  50
Division of B/A is :  2.0
Modules of A'%'B is : 5
Exponentiation of A**B is :  9765625
Floor division of A//B is :  0

ASSIGNMENT OPERATORS...
x = 10
x += 2  -> 12
x -= 2  -> 10
x *= 2  -> 20
x /= 2  -> 10.0
x %= 3  -> 1.0
x //= 3 -> 3
x **= 3 -> 1000
x &= 3  -> 2
x |= 3  -> 11
x ^= 3  -> 9
x >>= 2 -> 2
x <<= 2 -> 40

WALRUS OPERATOR...
3

COMPARISON OPERATORS...
x = 5, y = 1
5 < 1  -> False
5 > 1  -> True
5 <= 1 -> False
5 >= 1 -> True
5 == 1 -> False
5 != 1 -> True

LOGICAL OPERATORS...
The value of A and B is :  False
True
The value of A or B is :  True
True
The value of not b is :  True
False
True
False
True
True
'''