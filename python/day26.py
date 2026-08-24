'''def striker(a,b):
    assert a and b >0,"value should be greater than zero"
    return a+b
print(striker(5,6))
#
def game(a,b):
    assert b>0,"cannot be divided by zero"
    return a/b
print(game(3,7))
#
def KelvinToFahrenheit(Temperature): 
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32 
print (KelvinToFahrenheit(273))
print (int(KelvinToFahrenheit(505.78)))

def red(k):
    assert k>0,"greater than zero"
    return k*k*k
print(red(4))
#Cash withdraw
def speed(name,balance,withdraw):
    assert (balance>=withdraw),"insufficient balance unable to withdraw"
    return "Balance amount",balance,"Withdraw amount:",withdraw,"Current amount:",balance-withdraw
print(speed("striker",1024,24))
#
x={1,2,3,4}
y={3,4,5,6,7}
x^=(y)
print(x)'''
#
'''
file = open("file name",'mode')
'''

# modes
'''
x -> create a file
w -> write a file
a -> append a file
r -> read a file
'''
'''
## createing a file
#file = open("copy.txt",'x')
#print("file created sucessfully")
#file.close()<-used to close the file if it is opened
file=open("striker","x")
print("opened")
'''
'''
## writing a file
#file.close()<-used to close the file if it is opened
file = open("striker","w")
file.write("world")
file.close()


## append
#file.close()<-used to close the file if it is opened
file = open("striker","a")
file.write("(hello world)")
file.close()
'''
'''
#task
file = open("task2.txt", "a")
print("created")
name=True
while name:
    name = input("Enter the name: ")
    if name.lower() == "close":
        break
    date = int(input("Enter the date: "))
    year = int(input("Enter the birth year: "))
    file.write("\n")
    file.write("Name: ")
    file.write(name)
    file.write("\n")
    file.write("Age: ")
    file.write(str(date))
    file.write("\n")
    file.write("Year: ")
    file.write(str(year))
    file.write("\n")
file.close()'''
'''
#deleting a file
import os
os.remove("striker")
print("file soccessfully deleted")
'''
#task1
'''file = open("task2.txt", "a")
print("created")
name=True
while name:
    name = input("Enter the name: ")
    if name.lower() == "close":
        break
    date = int(input("Enter the date: "))
    year = int(input("Enter the birth year: "))
    file.write("\n")
    file.write("Name:")
    file.write("\t")
    file.write("Age:")
    file.write("\t")
    file.write("Year:")
    file.write("\n")
    file.write(name)
    file.write("\t")
    file.write(str(date))
    file.write("\t")
    file.write(str(year))
    file.write("\n")
file.close()'''
 



