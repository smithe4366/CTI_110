#CTI-110
#P4HW2
#Emanuel Smith
#11/30/2023
#Use if/else to determine an employees pay

#Create variables to hold totals paid to employees
num_em = 0
total_reg = 0
total_ot = 0
total_gross = 0 

emp_name= input("Enter employee name or type Done to quit: ")
#Loop to control adding employees
while emp_name != "Done":
    num_em += 1

    emp_hours= int (input("Enter employees hours: "))
    emp_pay = float(input("Enter employee pay rate: "))

    #Calculations
    if emp_hours > 40:
        ot_hours= emp_hours-40
        reg_hours = 40

    else: #This represents if emp_hours is 40 or less
        ot_hours = 0
        reg_hours = emp_hours
    #Calculate pay
    ot_pay= (emp_pay * 1.5) * ot_hours
    total_ot += ot_pay
    
    reg_pay = emp_pay * reg_hours
    total_reg += reg_pay
    
    gross_pay = ot_pay + reg_hours
    total_gross += gross_pay 

    print(f"Employee Name:  {emp_name} ")
    print(f"Regular Hours:  {reg_hours} ")
    print(f"OT Hours:  {ot_hours} ")
    print(f"Regular Pay:  {reg_pay} ")
    print(f"OT Pay:  {ot_pay} ")
    print(f"Gross Pay:  {gross_pay} ")
    print()
    emp_name= input("Enter employee name or type Done to quit: ")
    
#This code executes after look breaks
print("Done adding employees")
print()
print(f" Total number of employess: {num_em} ")
print(f" Total regular pay to employees: {total_reg}")
print(f" Total OT pay to employees: {total_ot} ")
print(f" Total Gross pay to employess: {gross_pay} ")

