'''def many(x,y):
    return x+y
a=many(10,21)
print(a)
#bank loan approval
def loan_check(age,salary,experience):
    if age>=21:
        if salary>=25000:
            if experience>2:
                return "Loan approved"
            else:
                return "rejected:experience must be greater than two years"
        else:
            return "rejected:salary must be greater than 25K"
    else:
        return "rejected:age must be atleast 21"

name=input("enter the name:")
age=int(input("enter the age:"))
salary=int(input("enter the monthly salary:"))
experience=int(input("enter the years of experience:"))

result=loan_check(age,salary,experience)

print("\n---LOAN DETAILS---")
print("Name:",name)
print("Age:",age)
print("Salary:",salary)
print("Experience:",experience)
print("Loan result:",result)'''


    












                                                     
    
















 
