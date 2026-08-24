def function(**val):
    print("name=",val["name"])
    print("age=",val["age"])
function(name="something",age=12)

#recurion
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    
  else:
    result = 0
    
  return result

print("\nRecursion Example Results")
print(tri_recursion(100))#50*101=5050

#without lambda
def lam(x,y):
    return x*y,x+y,x-y
print(lam(2,3))

#####with lambda 
lam = lambda x,y : x**y
print(lam(5,3))
#
same=lambda a,b:a*b
print(same(3,2))
#
same=lambda a,b:a+b
print(same(3,2))
#
same=lambda a,b:a-b
print(same(3,2))
#
mul=lambda k : "game "*k
print(mul(4))
#
import math
dif=lambda x :  math.factorial(x)
print(dif(7))
#
edo=lambda x:"even" if x%2==0 else "odd"
print(edo(4))
#
sty=lambda  k: "positive" if k>0 else "negative"
print(sty(-7))
#
deh=lambda x,y: x if x>y else y
print(deh(4,7))
#
deh=lambda x,y: x if x<y else y
print(deh(4,7))
#cube of a number
gta=lambda x:x*x*x
print(gta(3))
#
deh=lambda x,y: "equal" if x==y else "not equal"
print(deh(7,7))
#
deh=lambda x,y: "equal" if x==y else "not equal"
print(deh(7,4))
#mapping
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





