'''
x=int(input("enter the number:"))

if x>=50:
    if x>90:
        print("grade A")
        print("eligible for scholarship")
    else:
        if x>70:
            print("grader B")
            print("eligible for scholarship")
        else:
            print("grade C")
            print(" not eligible for scholarship")                 
else:
    print("failed the exam")
attendance=int(input("enter the  attendance percent:"))
mark=float(input("enter the CGPA:"))
income=int(input("enter the family income:"))

if attendance>=75:
    if mark>8.0 and income<300000:
        print("full scholarship")
    else:
        if mark>8.0 and income<600000:
            print("partial scholarship")
else:
    print("not eligible")
#

x=input("enter the data(student or premium member or others):")
y=int(input("enter the price:"))

if x == "student":
    if y>=50000:
        print("15% discount")
    else:
        print("10% discount")
else:
    if x == "premium member":
        print("5% discount")
    else:
        print("no discount")

#
year=input("student year(1,2,3,4):")
mark=float(input("enter the CGPA:"))
distance=int(input("enter the number of Km:"))
student=input("the student is physically disable(yes or no):")
rooms=input("whether hostel rooms are available(yes or no):")

if rooms == "yes":
    if student == "yes":
        print("allocate ground floor")
        if mark >= 8.5:
            print("single room")
        else:
            print("shared room")
    else:
        if distance >= 100:
            if year == "4":
                print("final year")
                if mark >= 8.0:
                    print("single room")
                else:
                    print("shared room")
            else:
                print("other year")
                if mark >= 8.0:
                    print("single room")
                else:
                    print("shared room")
                             
        else:
            if mark >= 9.5:
                print("single room")
            else:
                print("shared room")  
else:
    print("no rooms are available")'''

'''
name=input("enter the passenger name:")
age=int(input("enter the age:"))
travel=input("enter the mode of transport(bus/train/flight):")


if travel == "bus" and age>=0 and age<60:
    print("ticket available")
    print("no discount")
    dis=int(input("enter the kilometer:"))
    price=dis*5
    print("price amount:",price)
   
if travel == "bus" and age>=60:
    print("tickets available")
    dis=int(input("enter the kilometer:"))
    price=dis*5
    print("price amount:",price)
    dis=price-0.20
    print("discount amount:",dis)
    
   
if travel == "train" and age>=0 and age<60:
    print("no discount available")
    x=input("enter the coach(general/sleeper/ac):")
    if x=="general":
               dis=int(input("enter the kilometer:"))
               price=dis*5
               print("price amount:",price)
    if x=="sleeper":
               dis=int(input("enter the kilometer:"))
               price=dis*10
               print("price amount:",price)
    if x=="ac":
               dis=int(input("enter the kilometer:"))
               price=dis*15
               print("price amount:",price)
if travel == "train" and age>=60:
 print("20% discount available")
 x=input("enter the coach(general/sleeper/ac):")
 if x=="general":
               dis=int(input("enter the kilometer:"))
               price=dis*5
               print("price amount:",price)
               dis=price-0.20
               print("discount amount:",dis)
 if x=="sleeper":
               dis=int(input("enter the kilometer:"))
               price=dis*10
               print("price amount:",price)
               dis=price-0.20
               print("discount amount:",dis)
 if x=="ac":
                dis=int(input("enter the kilometer:"))
                price=dis*15
                print("price amount:",price)
                dis=price-0.20
                print("discount amount:",dis)
if travel == "flight" and age>=0 and age<60:
    print("no discount available")
    x=input("enter the coach(business,normal):")
    if x == "business":
        dis=int(input("display the kilometer:"))
        price=dis*15
        print("price amount:",price)
    if x == "normal":
         dis=int(input("enter the kilometer:"))
         price=dis*5
         print("price amount:",price)
if travel == "flight" and age>=60:
    print("20% discount available")
    x=input("enter the coach(normal /business)")
    if x == "business":
     dis=int(input("enter the kilometer:"))
     price=dis*15
     print("price amount:",price)
     dis=price-0.20
     print("discount amount:",dis)
    if x == "normal":
     dis=int(input("enter the kilometer:"))
     price=dis*15
     print("price amount:",price)
     dis=price*20/100
     discount=price-dis
     print("discount amount:",discount)
'''  
    
    

               











               
    

    
    
            
            
            
















   
        





        
        
        


        
            

        
