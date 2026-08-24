'''x=int(input("enter the number of students:"))
print("          ")
highest_total=0
highest_avg=0
highest_grade=""
top_student=""

grade_a=0
grade_b=0
grade_c=0
grade_d=0

for i in range(x):
    print("student:", i + 1)
    name=str(input("enter the name of the student:"))
    b=int(input("enter the attendance percentage:"))
    if b<75:
        print("==============================")
        print("##attendance percent was low##")
        print("==============================")
    else:
     if name[0].lower() in "aeiou":
         print("special category")
     k=int(input("enter the subject1 mark:"))
     L=int(input("enter the subject1 mark:"))
     N=int(input("enter the subject1 mark:")) 
     print("* * * * * * *")
     print("result for:",name)
     print("attendance percent:",b,"%")
     total=k+L+N
     print("total mark:",total,"/300")
     avg=total/3
     if avg>=85:
        print("grade A")
        grade="A"
        grade_a+=1
        print("     ")
     elif avg>=65:
        print("grade B")
        grade="B"
        grade_b+=1
        print("     ")
     elif avg>=50:
        print("grade C")
        grade="C"
        grade_c+=1
        print("     ")
     else:
        print("grade D")
        grade="D"
        grade_d+=1
        print("     ")      
     if total>highest_total:
       highest_total=total
       highest_avg=avg
       highest_grade=grade
       top_scorer=name
       
print("* * * FINAL RESULT * * *")
print("total number of students:",x)
print("top scorer:",top_scorer)
print("highest total:",highest_total)
print("highest average:",highest_avg)
print("highest grade:",highest_grade)
print("          ")
print("===GRADE COUNT===")
print("GRADE A:",grade_a)
print("GRADE B:",grade_b)
print("GRADE C:",grade_c)
print("GRADE D:",grade_d)

for i in range(1,6):
    if i == 3:
        continue
    print(i)

'''

















