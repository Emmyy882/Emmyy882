employee_Details = ["Empty"]

first_Name = input("Enter First Name: ")

second_Name = input("Enter Second Name: ")

other_Name = input("Enter Other Name: ")

employee_Details[0] = input("Enter Age: ")

email_Address = input("Enter Email Address: ")

phone_Number = input("Enter Phone Number: ")

address = input("Enter House Address: ")

levelOf_Edu = input("Enter Level Of Education: ")

InstitutionOf_Learning = input("Enter Institution Of Learning: ")

special_Skills = input("Enter Special Skills: ")



employee_Details.append(email_Address)

employee_Details.append(phone_Number)

employee_Details.append(address)

employee_Details.append(levelOf_Edu)

employee_Details.append(InstitutionOf_Learning)

employee_Details.append(special_Skills)


print("\nPERSONAL DETAILS: \n\n ")


print("\nFull Name: " + first_Name + " "  +second_Name + " " + other_Name)


print(employee_Details[0])

print(employee_Details[1])

print(employee_Details[2])

print(employee_Details[3])

print(employee_Details[4])

print(employee_Details[5])

print(employee_Details[6])

print("\n")

salary = float(input("Enter Salary: "))
pay_Period = int(input("Enter Number Of Pay Periods in A Year: "))
employee_Details.append(salary)
employee_Details.append(pay_Period)



''' To get Annual Salary we say,annual_Salary = salary * pay_Period '''
annual_Salary = float( employee_Details[7] * employee_Details[8] )
employee_Details.append(annual_Salary)

    
    
''' To get Gross pay, Gross pay = Annual Salary Amount / Number of Pay periods '''

gross_Pay = float( employee_Details[9] / employee_Details[8] )
employee_Details.append(gross_Pay)


''' To Get pay period Tax i.e Tax is only paid when Salary is received '''
if employee_Details[7] >= 100000 :
    pay_PeriodTax = 0.1 * employee_Details[7]
    employee_Details.append( pay_PeriodTax )
    
elif employee_Details[7] < 100000 :
    pay_PeriodTax = 0.05 * employee_Details[7]
    employee_Details.append( pay_PeriodTax )


''' Net Pay = Gross Pay - Taxes and Deductions '''
net_Pay = (employee_Details[10] - employee_Details[11] )
employee_Details.append(net_Pay)







print("\n")
print("Your Salary  is: " + str(employee_Details[7]))


print("Your pay period is: " + str(employee_Details[8]))

print("\n")
print("Annual Salary =\n Salary * Number of Pay Period = " + str(employee_Details[9]))



print("\n")
print("Gross Pay =\n Annual salary / Number of pay Period =  " + str(employee_Details[10]))

print("\n")
print("Your Tax per pay period is: " + str(employee_Details[11]))

print("\n")
print("Your Net Pay is: " + str(employee_Details[12]))



