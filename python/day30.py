#inheritance
# class that inherits all the methods and properties from another class.
""" 
Single Inheritance
Multiple Inheritance
Multilevel Inheritance
Hierarchical Inheritance
Hybrid Inheritance """
 
# Single Inheritance
#1
class parent:
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
    def func(self):
        print(f'{self.fname} {self.lname}')
a=parent('John', 'wick')
a.func()

class child(parent):
    pass
b=child("harry", "potter")
b.func()
a.func()
#2
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname1(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)# (or)self.firstname = fname
                                       #      self.lastname = lname

x = Student("Mike", "Olsen")
x.printname1()
#2
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname1(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

x = Student("Mike", "Olsen")
x.printname1()
#3
class Person1:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname2(self):
    print(self.firstname, self.lastname)

class Student2(Person1):
  def __init__(self, fname, lname):
    super().__init__(fname, lname) # inherit all the methods and properties from its parent.

x = Student2("Mike", "Olsen")
x.printname2()
##################
class new:
    def __init__(self,name,age,date,year):
        self.name=name
        self.age=age
        self.date=date
        self.year=year
    def green(self):
         print(f'information of the student name {self.name},age {self.age},date {self.date},year {self.year}')        
k=new("kkeerrtthhii",15,14,2008)
k.green()
del k.year
#k.green()
#################
# Multiple Inheritance

class division:
   def __init__(self, a,b):
      self.n=a
      self.d=b
   def divide(self):
      return self.n/self.d
   
class modulus:
   def __init__(self, a,b):
      self.n=a
      self.d=b
   def mod_divide(self):
      return self.n%self.d
      
class div_mod(division,modulus):
   def __init__(self, a,b):
      self.n=a
      self.d=b
   def div_and_mod(self):
      divval=division.divide(self)
      modval=modulus.mod_divide(self)
      return (divval, modval)
   
x=div_mod(5,5)
print ("division:",x.divide())
print ("mod_division:",x.mod_divide())
print ("divmod:",x.div_and_mod())
#













