mylist=[1,4,7,4,3,6,5,4,3]
print(len(mylist))
#
thislist = set(("apple", "banana", "cherry")) #change to set(curly bracket)
print(thislist)
#
thislist = list(("apple", "banana", "cherry"))#change to list
print(thislist)
#
mylist=[1,4,7,4,3,6,5,4,3]
print(mylist[-4])
#
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[-4:-1])
#
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[0:2] = ["star", "pink"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]#output:['apple', 'blackcurrant', 'watermelon', 'cherry']
print(thislist)
#***
thislist = ["apple", "banana", "cherry"]
thislist[1] = ["blackcurrant", "watermelon"]#output:['apple', ['blackcurrant', 'watermelon'], 'cherry']
print(thislist)
#***
thislist[1:3] = ["watermelon"]
print(thislist)
#type checking
mylist=["blue",1,True,3.14]
print(type(mylist[0]))
print(type(mylist[1]))
print(type(mylist[2]))
print(type(mylist[3]))
#insert element
listu=[1,6,85,86,56]
listu.insert(-0,True)
print(listu)
# Extend List
thislist = ["apple", "banana", "cherry"]
L=["pink","blue","black"]
thislist.extend(L)
print(thislist)
# Add Any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = {"kiwi", "orange"}
thislist.extend(thistuple)
print(thislist)
#,
# Add Any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
###
# Remove Specified Item

thislist = ["apple", "banana", "cherry",3.14]
thislist.remove(3.14)
print(thislist)

# Remove the first occurrence of "banana"
thislist = ["apple", "banana", "cherry", "banana", "kiwi",3,3,3]
thislist.remove(3)
print(thislist)

#pop
thislist = ["apple", "banana", "cherry"]
thislist.pop(0)#remove the element which is at the index position
print(thislist)

# Remove the last item
thislist = ["apple", "banana", "cherry",65,4,35,654]
thislist.pop(-1)
print(thislist)


# Remove the last item
thislist = ["apple", "banana", "cherry",65,4,35,654]
thislist.pop(-2)
print(thislist)

# Remove the first item
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Delete the entire list
thislist = ["apple", "banana", "cherry"]
del thislist
# Clear the List
mo = [75,97,45,34]
my=[75,97,45,34]
my.clear()
print(mo)
print(my)
# Sort the list alphabetically:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort the list numerically:

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort Descending
# To sort descending, use the keyword argument "reverse = True"
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# Sort the list descending

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
#used to reverse the list without ascending or descending
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
#copy a list
love=[14,1,2008,10,4]
dead=love.copy()
print(dead)
# Another way to make a copy is to use the built-in method list().
# Make a copy of a list with the list() method:

thislist = {"apple", "banana", "cherry"}
mylist = list(thislist)
print(mylist)

thislist = ("apple", "banana", "cherry")
mylist = list(thislist)
print(mylist)
# Make a copy of a list with the ':' operator

thislist = [2,6,4,2,5]
mylist = thislist[:]
print(mylist)
# Join Lists
# One of the easiest ways are by using the + operator.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Another way to join two lists is by appending all the items from list2 into list1, one by one:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

list1 = ["a", "b" , "c"]
list1.index("b")
print(list1)
#
mylist=[3,5,7,"pink",5,4]
my=mylist.index("pink")
print(my)
#
### List Comprehension
# List comprehension offers a shorter syntaxwhen you want to create a new list based on the values of an existing list.


# Syntax
# newlist = [expression for item in iterable if condition == True]

# Normal Way 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango","attribute"]

newlist = [x for x in fruits if "a" in x]

print(newlist)







