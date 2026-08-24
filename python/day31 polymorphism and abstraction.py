#polymorphism
class road:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def same(self):
    print("Drive!")

class water:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def same(self):
    print("Sail!")

class air:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def same(self):
    print("Fly!")

road1 = road("Ford", "Mustang")       
oat1 = water("Ibiza", "Touring 20") 
lane1 = air("Boeing", "747")     

for k in (road1,oat1, lane1):
  k.same()
  
#method overriding
class num1:
    def nodifference(self):
        print("calling superclass")
class num2(num1):
    def nodifference(self):
        print("calling subclass")

y=num1()
x=num2()
y.nodifference()
x.nodifference()

#method overloading
#Method Overloading means creating multiple methods with the same name
#but with different numbers or types of arguments
class example:
   def add(self, a, b):
      x = a+b
      return x
   def add(self, a, b, c):
      x = a+b+c
      return x

obj = example()
print (obj.add(14,4,7))
#using variable length argument(arbitary argument)
#(*args)
class Demo:
    def add(self, *args):
        print(sum(args))

obj = Demo()

obj.add(10, 20)
obj.add(10, 20, 30)
obj.add(10, 20, 30, 40,100)

#abstraction

from abc import ABC,abstractmethod

class pink(ABC):
    @abstractmethod
    def colour(self):
        pass

class blue(pink):
    def colour(self):
        return "goku black"

z=blue()
print(z.colour())
#
from abc import ABC,abstractmethod

class move(ABC):
    def __init__(self,name,place):
        self.name=name
        self.place=place

    @abstractmethod
    def same(self):
        pass
    def diff(self):
        print(f'name:{self.name},place:{self.place}')

class name(move):
    def same(self):
        print("invincible")
class place(move):
    def same(self):
        print("null releam")

flux=[name("goku","universe 7"),place("jiren","universe 11")]
for i in flux:
    i.diff()
    i.same()
#
from abc import ABC,abstractmethod

class move(ABC):
    def __init__(self,name,place,age):
        self.name=name
        self.place=place
        self.age=age

    @abstractmethod
    def same(self):
        pass
    def diff(self):
        print(f'name:{self.name},place:{self.place},age:{self.age}')

class name(move):
    def same(self):
        print("invincible")
class place(move):
    def same(self):
        print("null releam")

flux=[name("goku","universe 7",143),place("hit","universe 6",1000)]
for i in flux:
    i.diff()
    i.same()

#








        









        






