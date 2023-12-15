#Fisher Latravis (Jack)
#11/28/2023
#Use loop to get user input

from statistics import mean

num_grades = int(input("How many grades will you enter? "))

#Create a list to store the grades entered
grades_list=[]

#Get grades from user
for i in range (num_grades) :
     grade = float (input(f"Enter grade for module {i+1} : "))
     while grade < 0 or grade > 100:
        print (" You entered an invalid grade: ")
        grade = float (input(f"Enter grade for module {i+1} : "))
     grades_list.append(grade)

print(grades_list)


#Call methods on thelist to get results
list_sum = sum(grades_list)
list_avg=mean(grades_list)
lowest_grade=min(grades_list)
highest_grade=min(grades_list)

#create a value for spacing
x= " "

#Output to user with f-string
print("\n")
print("__________Results________")
print("Lowest Grade:", '     ',lowest_grade)
print("Highest Grade:", '     ',highest_grade)
print("Sum of Grades:", '     ', f"{list_sum:.2f}")
print("Average:",   '        ', f"{list_avg:2f}")
print("______________________________")
