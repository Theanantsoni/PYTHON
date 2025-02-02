#Croma Store Small Project ... python CS_project.py

print("------------------------------------------------------------------------")
print("-------------------------- Login Your Account --------------------------")

email = input("\nEnter Email ID : ")
Password = input("Enter Password : ")

if email == "123" or Password == "123":
	
	print("\n\n------------ You Are Login SuccessFully in Your Account ------------ ")
	print("------------------------------------------------------------------------")

	print("\nNo. \tProduct Name \t\t\tPrice \t\t Discount")
	print("1. \t Sony Bravia LED TV \t\t65800 \t\t 15%")
	print("2. \t Boat HeadPhone \t\t3000 \t\t 10%")
	print("3. \t Boat Speaker \t\t\t320000 \t\t 5%")
	print("4. \t Samsung Fridge \t\t45800 \t\t12%")
	print("5. \t Home Theator Speaker Set \t18600 \t\t20%")

	choice = int(input("\nPlease Enter the choice for buying the product : "))
	
	match choice:

		case 1:

			print("\nYou Select Number 1 Product")
			print("1. \t Sony Bravia LED TV \t\t65800 \t\t 5%")

			price = 65800;
			product = int(input("\nHow Many Product do you want ? : "))

			total = product * price
			print("\nTotal Price of The ", product ," is : ", total)

			discount = total * 15/100
			print("You Get Discount : ", discount)

			tot_dis = total - discount
			print("Total Price after Discount is : ", tot_dis)

			cgst = tot_dis * 6/100
			print("CGST amount is : ", cgst)

			sgst = tot_dis * 6/100
			print("SGST amount is : ", sgst)

			payment = total - discount + cgst + sgst
			print("You have to pay : ", payment)

			print("------------------------------------------------------------------------")

		case 2:

			print("\nYou Select Number 2 Product")
			print("2. \t Boat HeadPhone \t\t3000 \t\t 10%")

			price = 3000;
			product = int(input("\nHow Many Product do you want ? : "))

			total = product * price
			print("\nTotal Price of The ", product ," is : ", total)

			discount = total * 10/100
			print("You Get Discount : ", discount)

			tot_dis = total - discount
			print("Total Price after Discount is : ", tot_dis)

			cgst = tot_dis * 6/100
			print("CGST amount is : ", cgst)

			sgst = tot_dis * 6/100
			print("SGST amount is : ", sgst)

			payment = total - discount + cgst + sgst
			print("You have to pay : ", payment)

			print("------------------------------------------------------------------------")
		
		case 3:

			print("\nYou Select Number 3 Product")
			print("3. \t Boat Speaker \t\t\t320000 \t\t 5%")

			price = 32000;
			product = int(input("\nHow Many Product do you want ? : "))

			total = product * price
			print("\nTotal Price of The ", product ," is : ", total)

			discount = total * 5/100
			print("You Get Discount : ", discount)

			tot_dis = total - discount
			print("Total Price after Discount is : ", tot_dis)

			cgst = tot_dis * 6/100
			print("CGST amount is : ", cgst)

			sgst = tot_dis * 6/100
			print("SGST amount is : ", sgst)

			payment = total - discount + cgst + sgst
			print("You have to pay : ", payment)

			print("------------------------------------------------------------------------")

		case 4:

			print("\nYou Select Number 4 Product")
			print("4. \t Samsung Fridge \t\t45800 \t\t12%")

			price = 45800;
			product = int(input("\nHow Many Product do you want ? : "))

			total = product * price
			print("\nTotal Price of The ", product ," is : ", total)

			discount = total * 12/100
			print("You Get Discount : ", discount)

			tot_dis = total - discount
			print("Total Price after Discount is : ", tot_dis)

			cgst = tot_dis * 6/100
			print("CGST amount is : ", cgst)

			sgst = tot_dis * 6/100
			print("SGST amount is : ", sgst)

			payment = total - discount + cgst + sgst
			print("You have to pay : ", payment)

			print("------------------------------------------------------------------------")

		case 5:

			print("\nYou Select Number 5 Product")
			print("5. \t Home Theator Speaker Set \t18600 \t\t20%")

			price = 18600;
			product = int(input("\nHow Many Product do you want ? : "))

			total = product * price
			print("\nTotal Price of The ", product ," is : ", total)

			discount = total * 20/100
			print("You Get Discount : ", discount)

			tot_dis = total - discount
			print("Total Price after Discount is : ", tot_dis)

			cgst = tot_dis * 6/100
			print("CGST amount is : ", cgst)

			sgst = tot_dis * 6/100
			print("SGST amount is : ", sgst)

			payment = total - discount + cgst + sgst
			print("You have to pay : ", payment)

			print("------------------------------------------------------------------------")

		case _:

			print("You Entered Invalid Number ...")

else:

	print("\n\nFaild to Login Your Account... Please Try Again!!")