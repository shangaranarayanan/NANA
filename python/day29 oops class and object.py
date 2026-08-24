#class and objects
class name:
    K=14
    N='04'

c=name()
print(c.K)
print(c.N)
#
class sample:
    def __init__(simp,name,age):
        simp.name=name
        simp.age=age
k=sample("kkeerrtthhii",15)
print(k.name)
print(k.age)
#
class sample:
    def __init__(simp,name,age):
        simp.name=name
        simp.age=age
    def object(simp):
        l=7
        return l*l
    def night(simp):
        return "good bye"
k=sample("kkeerrtthhii",15)
print(k.name)
print(k.age)
print(k.object())
print(k.night())
c=sample("nana",17)
c.name="kkeerrtthhii"
print("\n",c.name)
print(c.age)
print(c.night())
print(c.object())
#
class bye:
    def __init__(simple,name,age):
        simple.name=name
        simple.age = age

    def sample(simple):
        simple.name="dd"
        simple.age=34
        return f'and my name is {simple.name},{simple.age}'
z=bye("krh",15)
z.age=17
print(z.name)
print(z.age)
print(z.sample())
print(z)

# classmethod(instance_method)"""
class Employee:
   empCount = 0
   def __init__(self, name, age):
      self.__name = name
      self.__age = age
      Employee.empCount += 1
   def showcount(self):
      print (self.empCount)                                            
   counter = classmethod(showcount)
e1 = Employee("Bhavana", 24)
e2 = Employee("Rajesh", 26)
Employee.counter()
#
class math:
    check=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        math.check+=1
    def list(self):
        print(self.check)

    count=classmethod(list)
k=math("krt",15)
n=math("nana",17)
s=math("sanjay",7)
math.count()
print(s.name,",",k.age)
