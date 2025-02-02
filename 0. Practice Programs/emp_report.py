#Employee Salary Report ... python emp_report.py

salary = float(input("Enter the Employee Salary : "))

hra = salary * 5/100
print("Employee HRA is : ", hra)

da = salary * 7 / 100 
print("Employee DA is : ", da)

travelling = salary * 2.5 / 100
print("Employee travelling amount is : ", travelling)

bonus = salary * 6 / 100
print("Employee Bonus amount is : ", bonus)

insuarance = salary * 3 / 100
print("Employee Insuarance amount is : ", insuarance)

pf = salary * 10 / 100
print("Employee PF amount is : ", pf)

total = salary + hra + da + travelling + bonus
print("Employee total salary is : ", salary)

net = total - insuarance - pf
print("Employee net amount is : ", net)
