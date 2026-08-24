#reference types
#iterator
k="14.01.2008"
n=iter(k)
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
#print(next(n))
#
print('')
#
class test:
    def __iter__(self):
        self.x=0
        return self
    def __next__(self):
        m=self.x
        self.x+=1
        return m
c=test()
no=iter(c)
print(next(no))
print(next(no))
print(next(no))
#
print('')
#
class num:
    def __iter__(self):
        self.n=0
        return self

    def __next__(self):
        if self.n<15:
            a=self.n
            self.n += 1
            return a
        else:
            raise StopIteration

b=num()
it=iter(b)

for i in it:
    print(i) 
#
print('')
#
fox = [1,7,4,14]
i=iter(fox)
while True:
    try:
        print(next(i))
    except StopIteration:
        print("iter has ended")
        break
#
print("")
#
#generator
def gen():
    yield "goku"
    yield "obito"
    yield "toji"
for x in gen():
    print(x)
#
def count(max):
    cut=0
    while cut<=max:
        yield cut
        cut += 1
cute=count(47)
for x in cute:
    print(x)

#
'''
def large_sequence(n):
  for i in range(n):
    yield i
# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(gen)'''
#
'''
def large_sequence(x,n):
  for i in range(x,n):
    yield i


gen = large_sequence(0,12)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
'''
#send() method
def echo():
    while True:
        x=yield
        print(x)
z=echo()
next(z)
z.send("goku")
z.send("black")

# close() Method
def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen))
print(next(gen))
gen.close()

#closure

def example1(name):
    name="obito"
    def example2():
        print(name)
    return example2
myfunction=example1("name")
myfunction()
#
def sample1():
    print("outer function")
    def sample2():
        print("inner function")
    sample2()
sample1()
#
def out(a):
    b=10
    def inn(c):
        return a+b+c
    return inn
x=out(2)
z=x(2)
print(z)
#

#decorator(ex)
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello"
print(myfunction())
#
def different(mat):
    def inside():
        return mat().lower()
    return inside
@different
def forever():
    return "UPPER"
print(forever())
#(ex)
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return f"Hello {func()} Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction())
#
def name(test):
    def fine():
       return test().upper()
    return fine

def date(test):
    def fine():
        return f'welcome to the {test()}'
    return fine

@name
@date
def notit():
    return 'hell'
print(notit())

