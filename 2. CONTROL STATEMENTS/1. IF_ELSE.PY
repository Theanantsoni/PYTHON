#equal or not-equal number ...
a=10
b=10
if a==b:
    print("Number is equal")
else:
    print("Number is not Equal")

#small & large number...
a=60
b=40
if a>b:
    print("A is bigger than B")
else:
    print("A is smaller than B")

#Voting...
age=19
if age>18 :
    print("You are eligible for voting...")
else :
    print("You are not eligible for voting...")

#Even or Add number...
no=2
if no%2==0 :
    print("Number is Even")
else :
    print("Number is Odd")

#AND OPERATOR...    //LOGICAL OPERATOR...
num=5
if num%5==0 and num%11==0 :
    print("Number is divisible with 5 & 11")
else :
    print("Number is not divisible with 5 & 11")

#OR OPERATOR... //LOGICAL OPERATOR...
x = 5
if x>1 or x<10 :
    print("Number between 1 to 10")
else :
    print("Number is not between 1 to 10")

#NOT OPERATOR...    //LOGICAL OPERATOR...
x = 5
if not(x>3 and x<10) :
    print("TRUE")
else :
    print("FALSE")
