'''
try:
    file = open("task2.txt", "r")
    content = file.read()
    print(content)
except:
    print("There is no such file")
finally:
    print("Program  successfully  execited")
'''
#
'''with open("task1.txt", "w") as file:
   file.write("Hello, World!")
   print ("Content0 added Successfully!!")'''
#or(file.close()<-is not needed)
'''file=open("task1.txt","w")
file.write("destroy world")
file.close()
print ("Content1 added Successfully!!") '''
#
'''
with open("task1.txt", "r+") as f:
  f.write("\nthis is the python code")
'''
#
'''file = open("task2.txt", 'r')
print("---read()---")
a = file.read()
print(a)
file.close()'''
#
'''import os

os.remove("task1.txt")
print("file successfully deleted")'''
#
# Try-Except Block
# used to handle exceptions and errors
# continue running even when something goes wrong.
'''
try:
   number = int(input("Enter a number: "))
   result = 10 / number
   print(f"Result: {result}")#or  print("Result:",result)
except ZeroDivisionError as e:
   print("Error: Cannot divide by zero.")

try:
   numerator = int(input("Enter the numerator: "))
   denominator = int(input("Enter the denominator: "))
   result = numerator / denominator
except ValueError:
   print("Error: Invalid input. Please enter valid integers.")
except ZeroDivisionError:
   print("Error: Cannot divide by zero.")
else:
   print(f"Result of division: {result}")

'''
'''
# Try-Finally Block
# ensure that certain code executes, regardless of whether an exception is raised or not.
# focuses on cleanup operations that must occur, ensuring resources are properly
#released and critical tasks are completed.

try:
    n = 
    res = 100 / n
    
except ZeroDivisionError:
    print("You can't divide by zero!")
    
except ValueError:
    print("Enter a valid number!")
    
else:
    print("Result is", res)
    
finally:
    print("Execution complete.")
'''














