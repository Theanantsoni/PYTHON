#STATIC RESULT PROGRAM...
ROLL_NO=1
NAME="ANANT"
C=91
CPP=93
JAVA=95
PHP=97
PYTHON=99

TOT=C+CPP+JAVA+PHP+PYTHON
PER=TOT/5
print("\n\nSTATIC PROGRAM GENERATED.....")
print("Student Roll Number is : " ,ROLL_NO)
print("Student Name is : " ,NAME)

print("C language marks is : " ,C)
print("C++ language marks is : " ,CPP)
print("JAVA language marks is : " ,JAVA)
print("PHP language marks is : " ,PHP)
print("PYTHON language marks is : " ,PYTHON)

print("Total marks is : " ,TOT ,"/ 500")
print("Percentage is : " ,PER)



#DYNAMIC RESULT PROGRAM...
print("\n\nDYNAMIC PROGRAM GENERATED.....")
#take an input for Student Details...
roll_no=input("Enter a Student Roll Number : ")
name=input("Enter Student a Name : ")

c=int(input("Enter a C language marks : "))
cpp=int(input("Enter a C++ language marks : "))
java=int(input("Enter a JAVA language marks : "))
php=int(input("Enter a PHP language marks : "))
python=int(input("Enter a PYTHON language marks : "))

#Display an output for Student Details...
print("Student Roll no. is : " ,roll_no)
print("Student Name is : " ,name)

print("C language marks is : " ,c)
print("C++ language marks is : " ,cpp)
print("JAVA language marks is : " ,java)
print("PHP language marks is : " ,php)
print("PYTHON language marks is : " ,python)

#Total,percentage...
tot=(c+cpp+java+php+python)
per=(tot/5)

#Display
print("total marks is : " ,tot, "/ 500")
print("Percentage is : " ,per)
