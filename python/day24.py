'''k={}
k1=[]
num=int(input("number of student:"))
for i in range(num):
 name=str(input("enter the name:"))
 mark=int(input("enter the mark:"))
 mark1=int(input("enter the mark:"))
 mark2=int(input("enter the mark:"))
 mark3=int(input("enter the mark:"))
 mark4=int(input("enter the mark:"))
 k1.append(mark)
 k1.append(mark1)
 k1.append(mark2)
 k1.append(mark3)
 k1.append(mark4)
print(k1)'''
#output:{'jk': [54, 56, 28, 91, 37], 'dd rayan': [54, 56, 52, 52, 32], 'tr': [54, 56, 52, 12, 32]}
'''k={}
num=int(input("Number of students:"))
print("")
for K in range(num):
    name=input("Enter the name:")
    print("")
    mark1=[]
    for N in range(5):
        mark=int(input("Enter the mark:"))
        mark1.append(mark)
    k[name]=mark1
print(k)'''
#stacks
st=[]
st.append("black goku")
st.append("obito")
st.append("goku")
st.append("toji")
print(st)
x=st[-3]
print(x)
z=st.pop(-2)
print(z)
y= not bool(st)
print(y)
print(len(st))
#queues
x=st[1]
print(x)
c=st.pop(1)
print(c)

