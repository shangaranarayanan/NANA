'''#mapping
#cube
def fun(k):
    return k*k*k

n = [1,2,3,4,5]

for i in n:
    print(i*i*i)

z = list(map(fun,n))
print(z)
#

#square
def fun(k):
    return k*k

n = [1,2,3,4,5]

for i in n:
    print(i*i)

z = list(map(fun,n))
print(z)
#
def god(r):
    return r-6
k=[1,2,3,4,5]

x=list(map(god,k))
print(x)
#
def ang(v):
    return v+10
x=[4,7,3]
f=list(map(ang,x))
print(f)
#
ang=lambda v:v+10
x=[4,7,6,]
f=list(map(lambda v:v+10,x))
print(f)
#
print("FACTORIAL")
import math
dif=lambda x :  math.factorial(x)
v=[6,7,3,4,5,2]
f=list(map(lambda x :  math.factorial(x),v))
print(f)
#
print("    ")
#quotient
asus=lambda a : a/5
x=[1,4,3,6,5,7,2]
k=list(map(lambda a : a/5,x))
print(k)
#remainder
asus=lambda a : a/5
x=[1,4,3,6,5,7,2]
k=list(map(lambda a : a%5,x))
print(k)
#power 
asus=lambda a : a**5
x=[1,4,3,6,5,7,2]
k=list(map(lambda a : a**5,x))
print(k)
#
edo=lambda x: x%2==0 
u=[2,3,4,7,6,1,17]
h=list(map(lambda x: x%2==0 ,u))
print(h)
#
edo=lambda x: x>0
u=[-2,3,4,-7,6,1,-17]
h=list(map(lambda x:x>0 ,u))
print(h)
#
edo=lambda x: x==2
u=[2,3,4,7,2,1,2]
h=list(map(lambda x: x==2 ,u))
print(h)'''
#
fun=lambda x: x in "aeiou"

string=["a","S","g","f","i","l"]
h=list(filter(lambda x: x in "aeiou",string))
print(h)
#
stu=["star","Big","pink","Black","orange"]
k=list(filter(lambda x:x.islower(),stu))
print(k)
#
x=[1,2,3,4,5,6,7,8,9,10]
z=list(filter(lambda y:y%2==0,x))
print(z)
#
x=[1,2,3,4,5,6,7,8,9,10]
z=list(filter(lambda y:y%2!=0,x))
print(z)
#
x=[-1,2,-3,4,-5,6,-7,8,-9,10]
z=list(filter(lambda y:y>0,x))
print(z)
#
x=[-1,2,-3,4,-5,6,-7,8,-9,10]
z=list(filter(lambda y:y<0,x))
print(z)
#
x=[12,21,34,32,47,52,76,72]
z=list(filter(lambda y:y==max(x) ,x))
print(z)










