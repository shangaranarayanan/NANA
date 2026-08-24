try:
 a=int(input("a:"))
 b=int(input("b:"))
 print(a-b)

except ValueError:
    print("enter only numbers")
finally:
    print("executed successfully")
#
print("  ")
#
try:
 k=[1,2,3,4,5,6,7,8,12,16,14,17]
 print(k[47])
except IndexError:
    print("no such index number exist")
finally:
    print("value found successfully")
#
print("")
#
try:
 def add(a,b):
    print(a+b)
 print(sub(2,4))
except NameError:
    print("function name not found")
finally:
    print("executed successfully")
#
print("")
#

