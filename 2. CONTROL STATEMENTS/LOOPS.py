'''Python Loops
Python has two primitive loop commands:
1. while loops
2. for loops'''

#LOOPS : 
#While Loop :
print("\n\nWHILE LOOP 1 : ")
i=1
while i<=5 :
    print(i)
    i+=1

print("\n\nWHILE LOOP 2 : ")
y = 1
while y < 6:
  print(y)
  y += 1
else:
  print("y is no longer less than 6")

#-------------------------------------------

#For Loop :
print("\n\nFOR LOOP 1 : ")
for x in range(6):
  print(x) 

print("\n\nFOR LOOP 2 : ")
for j in range(1,5) :
    print(j)

print("\n\nFOR LOOP 3 : ")
for x in range(2, 30, 3):
  print(x) 

print("\n\nFOR LOOP 4 : ")
for x in range(6):
  print(x)
else:
  print("Finally finished!")

print("\n\nFOR LOOP 5 : ")
num1 = ["1", "2", "3"]
num2 = ["3", "4", "5"]

for x in num1:
  for y in num2:
    print(x, y)