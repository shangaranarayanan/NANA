def add(a,b):
    print(a + b)
add(17,34)

def sub(x,y):
    print(x-y)
sub(3,7)

def mul(K,N):
    print(K*N)
mul(14,4)

def div(z,x):
    print(z/x)
div(7,4)

def div(z,x):
    print(z/x)
pow(14,4)


def fact(k):
 import math
 n=math.factorial(k)
 print("factorial of",k,":",n)
fact(10)
fact(7)
#
print("        ")

def aev(x):
    if x%2 == 0:
        print("even number")
    else:
        print("odd number")
aev(17)
aev(12)
#
print("    ")

def top(x,y):
    if x>y:
        print("x is greater")
    elif x<y:
        print("y is greater")
    else:
        print("x and y are equal")
top(4,7)
top(1,1)

#
print("    ")

def stu(a,b,c,d):
    print("         ")
    print("Name of the student:",a)
    print("Roll No of the student;",b)
    print("student college:",c)
    print("Department of the student:",d)
    
stu("tarun",3566765,"psg","cse")
stu("rohith",3566331,"ajc","eee")
stu("sathish",3566001,"cit","cse(AI)")
stu("shankar",3566334,"CIT","cse")

def stu(x,y,z):
    print("       ")
    print("subject1:",x)
    print("subject2:",y)
    print("subject3:",z)
    a=x+y+z
    print("total:",a)
    b=a/3
    print("average:",b)
    print("   ")
stu(100,93,87)

#
def num(k,n):
    for i in range(k,n):
        print(i)
num(1,11)
#
print("    ")
#
def num(k,n,s):
    for i in range(k,n,s):
        print(i)
num(1,11,1)
#
print("    ")
#
def num(k,n,s):
    for i in range(k,n,s):
        print(i)
num(20,0,-2)
#
print("     ")
#
def tab(x):
    print("tables:",x)
    for i in range(1,21):
        print(i,"X",x,"=",i*x)
tab(2)
#
print("      ")
#
def gde(x):
    print("marks:",x)
    if x>90 and x<=100:
        print("grade A")
    elif x>80 and x<=90:
        print("grade B")
    elif x>70 and x<=80:
        print("grade C")
    elif x>60 and x<=70:
        print("grade D")
    else:
        print("grade E")
gde(76)
#
