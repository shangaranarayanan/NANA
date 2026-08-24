#encapsulation
class new:
    def __init__(self,place="ooty",time=2024):
      self.place=place
      self.time=time

x=new("chennai","2026")

print("place: {}\ntime: {}".format(x.place,x.time))
#
class new:
    def __init__(self,place="ooty",time=2024):
      self.place=place
      self.time=time

x=new()
z=new("kumbakonam","0000")
print("place: {}\ntime: {}".format(x.place,x.time))
print("place: {}\ntime: {}".format(z.place,z.time))
#public member(ex)
class Employee:
    def __init__(self, name):
        self.name = name   # public attribute

    def display_name(self):   # public method
        print(self.name)

emp = Employee("John")
emp.display_name()   # Accessible
print(emp.name)      # Accessible
#public
class label:
    def __init__(self,record,date,place):
        self.record=record
        self.date=date
        self.place=place

    def who(self):
        print(self.record)
        print(self.date)
        print(self.place)
k=label("squad wipe",14,"park")
k.who()#accessible
print(k.record)#accessible
print(k.date)


#protected member(ex)[ Accessible only in subclass]
class Employee:
    def __init__(self, name, age):
        self.name = name       # public
        self._age = age        # protected

class SubEmployee(Employee):
    def show_age(self):
        print("Age:", self._age)   # Accessible in subclass

emp = SubEmployee("Ross", 30)
print(emp.name)        # Public accessible
emp.show_age()

#protected [ Accessible only in subclass]  {(_)is refers to protected}
class new:
    def __init__(self,name,date,place):
        self.name=name
        self._date=date
        self.place=place
class old(new):
    def next(self):
        print(f'name:{self.name}\ndate:{self._date}\nplace:{self.place}')
        
z=old("k",14,"park")
z.next()
print(z.place)
print(z._date)
#z.place()# Protected accessed through subclass

#Private members(ex)[accessed through the same class]
#{(__) is refered to private}
class Employee:
    def __init__(self, name, salary):
        self.name = name          # public
        self.__salary = salary    # private

    def show_salary(self):
        print("Salary:", self.__salary)

emp = Employee("Robert", 60000)
print(emp.name)          # Public accessible
emp.show_salary()        # Accessing private correctly
# print(emp.__salary)    # Error: Not accessible directly

#private[in private we cannot get particular name(or)place]
class speed:
    def __init__(self,name,date):
        self.__name=name
        self.date=date
    def int(self):
        print(f'name:{self.__name}\ndate:{self.date}')
c=speed("k",4)
#print(c.__name)# Error: Not accessible directly
print(c.date)
c.int()

# Getter and Setter(used only for private class member)
class Employee:
    def __init__(self):
        self.__salary = 50000  # Private attribute

    def get_salary(self):    # Getter method
        return self.__salary

    def set_salary(self, amount):   # Setter method 
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary amount!")
emp = Employee()
print(emp.get_salary())  # Access salary using getter

emp.set_salary(60000)   # Update salary using setter
print(emp.get_salary())

#
class new:
    def __init__(self):
        self.__salary=1000
    def int(self):
        return self.__salary
    def take(self,amount):
        if amount>0:
            self.__salary=amount
        else:
            pass
x=new()
print(x.int())#accessing salary using getter(getting the particular information)

x.take(475620)
print(x.int())





