# Student Result ... python st_result.py

c = int(input("Enter the C language marks : "))
cpp = int(input("Enter the cpp language marks : "))
java = int(input("Enter the java language marks : "))
php = int(input("Enter the php language marks : "))
python = int(input("Enter the python language marks : "))

total = c + cpp + java + php + python
print("Your Total marks is : ", total ,"Out of 500")

percentage = total * 100 / 500
print("Your Percentage is : ", percentage)

if c < 40 or cpp < 40 or java < 40 or php < 40 or python < 40:
	print("You Are Failed Successfully... Ready for give ATKT exam 😂")
else:
	if percentage >= 80 and per <= 100:
		print("You Got Distinction...")
	elif percentage >= 70 and percentage < 80:
		print("You Got First Class...")
	elif percentage >= 60 and percentage < 70:
		print("You Got Second Class...")
	elif percentage >= 50 and percentage < 60:
		print("You Got Third Class...")
	elif percentage >=40 and percentage < 50:
		print("You are Mand Mand Pass...")
	else:
		print("You Are Faild...")


