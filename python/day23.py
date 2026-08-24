'''
# isdisjoint()	 	    Returns whether two frozensets have an intersection	
# issubset()	<= / <	Returns True if this frozenset is a (proper) subset of another	
# issuperset()	>= / >	Returns True if this frozenset is a (proper) superset of another	

a = {1,2,3,4,5,6,7,8}
b = {1,2,3,55}

print(b.issubset(a))

#
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1969
}
print(thisdict["brand"])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

print(len(thisdict))

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

x = thisdict.get("country")
print(x)

print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
car["color"] = "white"
print(car)

thisdict["year"] = 2015

thisdict.update({"year": 2020})

print(thisdict)

car.pop("model")
print(car)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

del thisdict["model"]
print(thisdict)
del thisdict
#print(thisdict)
#thisdict.clear()

thisdict = dict(name = "John", age = 36, country = "Norway")
for x in thisdict.values():
  print(x)

for x in thisdict.keys():
  print(x)

for x, y in thisdict.items():
  print(x, y)

mydict = thisdict.copy()
print(mydict)

mydict = dict(thisdict)
print(mydict)
'''
'''#
x={"name":"k","age":"17","year":"2006","year":"2007","year":"2008"}
print(x)

print(len(x))
#
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
#
thisdict = dict(name = "black goku", age = 36, country = "Norway")
print(thisdict)
#
thisdict = dict(name = "John", age = 36, country = "america")
print(thisdict)

x = thisdict.get("country")
print(x)
print(x["name"])
print(thisdict["brand"])

###
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

x = thisdict.get("country")
print(x)

print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())
###


#adding new key:value pair(new value)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}



#
car.pop("model")
print(car)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
#
'''
'''
#
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}

del thisdict["model"]
print(thisdict)

thisdict = dict(name = "John", age = 36, country = "Norway")
for x in thisdict.values():
  print(x)
print("")

for x in thisdict.keys():
  print(x)
print("")
for x, y in thisdict.items():
  print(x, y)
print("")
mydict = thisdict.copy()#copy the dictionary
print(mydict)

mydict = dict(thisdict)#another way to copy dictionary
print(mydict)
#
'''
# Nested Dictionaries



child1 = {"name" : "Emil","year" : 2004}
child2 = {"name" : "Tobias","year" : 2007}
child3 = { "name" : "Linus","year" : 2011}

myfamily = {"1" : child1,"2" : child2}
print(myfamily)
































