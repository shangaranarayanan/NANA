
'''k=[]
highest=0
names=[]
x=int(input("no of students:"))
for i in range(x):
    name=str(input("name:"))
    mark=int(input("mark:"))
    k.append([name,mark])
    if mark>highest:
        highest=mark
        names=[name]
    elif mark==highest:
        names.append(name)
names.sort()
print(k)
print("student:",names)
print("max mark:",highest)'''
'''
#
## Set
# sequence inside curly braces{}
# A set is a collection which is unordered, unchangeable, and unindexed.
#set does not allow any duplicates

thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

thisset = {"apple", "banana", "cherry", False, True, 0, 1, 2} # 1==True, 0==False
print(thisset)

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}

thisset = set(("apple", "banana", "cherry"))#change tuple to set 
print(thisset)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
print("banana" not in thisset)

thisset.add("orange")
print(thisset)


tropica = {"pineapple", "mango", "papaya"}
thisset.update(tropica)
print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)
print(thisset)

thisset.remove("banana") # if item not exist raise error
print(thisset)

thisset.discard("banana") # if item not exist not raise error
print(thisset)

x = thisset.pop()
print(x)
print(thisset)

thisset.clear()
print(thisset) 

### del thisset
### print(thisset)
##
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
##
##set3 = set1 | set2 #use the | operator instead of the union()
##print(set3)
##
##set1 = {"a", "b", "c"}
##set2 = {1, 2, 3}
##set3 = {"John", "Elena"}
##set4 = {"apple", "bananas", "cherry"}
##
##myset = set1.union(set2, set3, set4)
##myset1 = set1 | set2 | set3 |set4
##print(myset)
##print(myset1)
##
##x = {"a", "b", "c"}
##y = (1, 2, 3)
##
##z = x.union(y)
##print(z)
##
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
##
### The intersection() method will return a new set,
### that only contains the items that are present in both sets.
##
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
set4 = set1 & set2
print(set3)
print(set4) 
##
### The intersection_update() method will also keep ONLY the duplicates, 
### but it will change the original set instead of returning a new set.
##set1 = {"apple", "banana", "cherry"}
##set2 = {"google", "microsoft", "apple"}
##
##set1.intersection_update(set2)
##
##print(set1)
##
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
# set3 = set1 - set2
print(set3)
##
##set1 = {"apple", "banana", "cherry"}
##set2 = {"google", "microsoft", "apple"}
##
##set3 = set1.s
##(set2)
##set3 = set1 ^ set2
##print(set3)
##
### Set Methods
##"""
##add()	 	            Adds an element to the set
##clear()	 	            Removes all the elements from the set
##copy()	 	            Returns a copy of the set
##difference()	    -	Returns a set containing the difference between two or more sets
##difference_update()	-=	Removes the items in this set that are also included in another, specified set
##discard()	 	        Remove the specified item
##intersection()	    &	Returns a set, that is the intersection of two other sets
##intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
##isdisjoint()	 	    Returns whether two sets have a intersection or not
##issubset()	        <=	Returns True if all items of this set is present in another set
## 	                <	Returns True if all items of this set is present in another, larger set
##issuperset()	    >=	Returns True if all items of another set is present in this set
## 	                >	Returns True if all items of another, smaller set is present in this set
##pop()	 	        Removes an element from the set
##remove()	 	    Removes the specified element
##symmetric_difference()	^	Returns a set with the symmetric differences of two sets
##symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
##union()	            |	Return a set containing the union of sets
##update()	        |=	Update the set with the union of this set and others"""
##
#### frozenset
### Unlike sets, elements cannot be added or removed from a frozenset.
##
##x = frozenset({"apple", "banana", "cherry"})
##print(x)
##print(type(x))

# Frozenset Methods
# copy()	 	        Returns a shallow copy	
# difference()	    -	Returns a new frozenset with the difference	
# intersection()	&	Returns a new frozenset with the intersection	
# isdisjoint()	 	    Returns whether two frozensets have an intersection	
# issubset()	<= / <	Returns True if this frozenset is a (proper) subset of another	
# issuperset()	>= / >	Returns True if this frozenset is a (proper) superset of another	
# symmetric_difference()	^	Returns a new frozenset with the symmetric differences	
# union()	        |	Returns a new frozenset containing the union

#
to create a empty set type x=set()
set() is considered as empty set instead of {}
#
'''
'''#
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
myset1 = set1 | set2 | set3 |set4
print(myset)
print(myset1)
#
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
set1.union(set2)
print(set1)

#
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
set4 = set1 & set2
print(set3)
print(set4)
#
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)
#
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.union(set2)
print(set3)


set1.update(set2)
print(set1)

set1.difference_update(set2)
print(set1)'''
#without repetition
k=[]
no=int(input("enter the number:"))
for i in range(no):
    name=str(input("enter the name:"))
    k.append(name)
x=set((k))
print(x)
#

 
    
    



