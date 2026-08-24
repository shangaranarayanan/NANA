#task2

file = open(".txt", "w")
file.write("\n")
file.write("Name:")
file.write("\t")
file.write("Age:")
file.write("\t")
file.write("Year:")
name=True
while name:
    name = input("Enter the name: ")
    if name.lower() == "close":
        break
    date = int(input("Enter the date: "))
    year = int(input("Enter the birth year: "))
    file.write("\n")
    file.write(name)
    file.write("\t")
    file.write(str(date))
    file.write("\t")
    file.write(str(year))
    file.write("\n")
file.close()
#task1
'''file = open("task2.txt", "a")
print("created")
name=True
while name:
    name = input("Enter the name: ")
    if name.lower() == "close":
        break
    date = int(input("Enter the date: "))
    year = int(input("Enter the birth year: "))
    file.write("\n")
    file.write("Name:")
    file.write("\t")
    file.write("Age:")
    file.write("\t")
    file.write("Year:")
    file.write("\n")
    file.write(name)
    file.write("\t")
    file.write(str(date))
    file.write("\t")
    file.write(str(year))
    file.write("\n")
file.close()'''
#
file = open("task2.txt", "a")











 
