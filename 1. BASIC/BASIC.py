#\n=new Line	
#\t=tab\space
#Single line comment..
'''Multiple line comment...'''

print("Hello World")
print("Good morning")	
print("Good Afternoon")
print("Good Evening")

#Set a variables...#Static
str_value="ANANT"
int_value=10
float_value=15.25

#display Static variables ... 
print("\nStatic Variable value printed...")
print("String value is : " ,str_value)
print("Integer value is : " ,int_value)
print("Float value is : " ,float_value)

#Get Dynamic value from user ...
Str_value = input("\nEnter a string value: ")  # Input is already a string
Integer_value = int(input("Enter an integer value: "))  # Convert input to integer
Float_value = float(input("Enter a float value: "))  # Convert input to float

#display Dynamic variables ... 
print("\nDynamic Variable value printed...")
print("String value is : " ,Str_value)
print("Integer value is : " ,Integer_value)
print("Float value is : " ,Float_value)

#printing multi line string ...
print('''\nhello
good morning
python program''')

#printing escaping characters
print("\nSoni \"Anant\" Rajeshkumar")

#Check multiple argument...
a="hello"
b="python program"

print("\nMultiple Argument is : " ,a,b)

