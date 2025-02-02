#Check positive,negative or zero number...
a=0
if a>0 :
    print(a,"Number is positive")
elif a<0 :
    print(a,"Number is negative")
else :
    print(a,"Number is Zero")

#Result...
per=36;
if per>90 and per<=100 :
    print("Percentage is : ",per," you got Distinction")
elif per>80 and per<=90 :
    print("Percentage is : ",per," You got First class")
elif per>70 and per<=80 :
    print("Percentage is : ",per," You got second class")
elif per>60 and per<=70 :
    print("Percentage is : ",per, " You got Third class")
elif per>50 and per<=60 :
    print("Percentage is : ",per," You got Fourth class")
elif per>40 and per<=50 :
    print("Percentage is : ",per," You got Fifth class")
elif per>33 and per<=40 :
    print("Percentage is : ",per," You are pass")
else :
    print("You are Fail")