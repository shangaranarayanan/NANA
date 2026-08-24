# Listbox
'''from tkinter import *
top = Tk()
Lb = Listbox(top)
Lb.insert(1, 'Python')
Lb.insert(2, 'Java')
Lb.insert(3, 'C++')
Lb.insert(4, 'Any other')
Lb.pack()
top.mainloop()''' 
#or
'''from tkinter import *
top = Tk()
Lb = Listbox(top)
Lb.insert(END, "Python")
Lb.insert(END, "Java")
Lb.insert(END, "C++")
Lb.insert(END, "Any other")
Lb.pack()
top.mainloop()'''

'''
# Scrollbar
#TAS.pack(side=RIGHT, fill=X)
#mylist = Listbox(root, xscrollcommand=TAS.set)
from tkinter import *
root = Tk()
TAS = Scrollbar(root)
TAS.pack(side=RIGHT, fill=Y)
mylist = Listbox(root, yscrollcommand=TAS.set)

for line in range(100):
    mylist.insert(END, 'This is line number' + str(line))
mylist.pack(side=LEFT, fill=BOTH)
TAS.config(command=mylist.yview)
root.mainloop()'''
'''
# Menu
#root.config(menu=menu)<-Without this line, the menu bar would not appear.
from tkinter import *
root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')
mainloop()
'''
#*listbox
'''from tkinter import *
task=Tk()
Lb=Listbox(task)
Lb.insert(1,"goku")
Lb.insert(2,"obito")
Lb.insert(3,"toji")
Lb.insert(4,"divine general")
Lb.pack()
ch.mainloop()'''

'''
#*scrollbar
from tkinter import *
ch = Tk()
TAS = Scrollbar(ch)
TAS.pack(side=RIGHT,fill=Y)
mylist=Listbox(ch,yscrollcommand=TAS.set)

for i in range(48):
    mylist.insert(END,'this is line' + str(i))
mylist.pack(side=LEFT,fill=BOTH)
TAS.config(command=mylist.yview)
ch.mainloop()
'''
'''
#menu
from tkinter import *
root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')
root.mainloop()
'''
'''
#submenus
from tkinter import *
root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)
newmenu = Menu(filemenu, tearoff=0)
filemenu.add_cascade(label="New", menu=newmenu)
newmenu.add_command(label="Text File")
newmenu.add_command(label="Python File")
newmenu.add_command(label="Folder")
filemenu.add_command(label="Open...")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About")
root.mainloop()
'''
'''
#
from tkinter import *
root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)
newlist = Menu(filemenu, tearoff=0)
filemenu.add_cascade(label="New", menu=newlist)
newlist.add_command(label="file1")
newlist.add_command(label="file2")
newlist.add_command(label="file3")
filemenu.add_command(label="Open...")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About")
root.mainloop()
'''
'''
#canvas
import tkinter as tk

root = tk.Tk()
root.title("Print ")

canvas = tk.Canvas(root, width=300, height=200, bg="black")
canvas.pack()

canvas.create_text(150, 100, text="BGMI", font=("Ink Free", 20), fill="green")

root.mainloop()
'''

'''
import tkinter as tk

root = tk.Tk()
root.title("Print")

canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack()

canvas.create_text(150, 100, text="BGMI", font=("Ink Free", 20), fill="green")

canvas.create_line(100,105,200,105, fill="black" ,width=2)

canvas.create_rectangle(90,80,220,120, fill="red", outline="black")

canvas.create_oval(135,80,175,120, fill="yellow", outline="black")

canvas.create_arc(90,10,220,100, start=0, extent=180, width=3,  style=tk.ARC)

canvas.create_polygon(100,180,150,100,200,180, fill="red")

root.mainloop()
'''
'''
import tkinter as tk

root = tk.Tk()
root.title("Print")

canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack()

canvas.create_rectangle(90,80,220,120, fill="red", outline="black")

canvas.create_oval(135,80,155,100, fill="yellow", outline="black")
'''
'''
#car
import tkinter as tk
root = tk.Tk()
root.title("monster truck")
canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack()

canvas.create_rectangle(150, 180, 450, 260, fill="blue", outline="black")

canvas.create_polygon( 280, 180,270, 120,370, 120,420, 180,fill="skyblue",outline="black")

canvas.create_oval(190, 240, 260, 310, fill="black")
canvas.create_oval(340, 240, 410, 310, fill="black")

root.mainloop()
'''
'''
#emoji
import tkinter as tk
root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500, bg="white")
canvas.pack()

canvas.create_oval(100, 100, 400, 400, fill="yellow", outline="black")

canvas.create_oval(160, 180, 200, 220, fill="black")

canvas.create_oval(300, 180, 340, 220, fill="black")

canvas.create_arc(200, 250, 300, 350, start=180, extent=180, width=2)

canvas.create_polygon(170, 120,   330, 120,  250, 20,    fill="red",outline="black",width=2)

canvas.create_oval(240, 5, 260, 25, fill="blue",outline="green")
'''
'''
#
import tkinter as tk
root = tk.Tk()
root.title("Live Train Moving Status")
root.geometry("400x300")
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()
canvas.create_rectangle(50, 180, 200, 220, fill="red")
canvas.create_rectangle(200, 165, 260, 220, fill="darkred")
canvas.create_oval(70, 215, 100, 245, fill="black")
canvas.create_oval(150, 215, 180, 245, fill="black")
canvas.create_oval(210, 215, 240, 245, fill="black")
root.mainloop()'''
'''
#program for moving an object
import tkinter as tk
root = tk.Tk()
root.title("moving objuct")
can = tk.Canvas(root, height=500, width = 800, bg = "white")
can.pack()
a = can.create_oval(-100,200,0,300, fill = "lightgreen", outline="green")

def mv():
    
    can.move(a,5,0)#5 refers to pixel in x axis and 0 in y axis
    can.after(10,mv)# 10 refers to milisecond and mv to call the loop again and again
    
mv()
root.mainloop()
'''

'''
#moving truck 
import tkinter as tk
root = tk.Tk()
root.title("moving object")
can = tk.Canvas(root, height=500, width = 800, bg = "white")
can.pack()
a =[can.create_rectangle(50, 180, 200, 220, fill="red"),
can.create_rectangle(200, 165, 260, 220, fill="darkred"),
can.create_oval(70, 215, 100, 245, fill="black"),
can.create_oval(150, 215, 180, 245, fill="black"),
can.create_oval(210, 215, 240, 245, fill="black")]
can.create_rectangle(0,245,800,500,fill="grey")
def mv():
    for i in a:
      can.move(i,5,0)
    can.after(10,mv)
mv()
root.mainloop()
'''
'''
#moving train
import tkinter as tk
root = tk.Tk()
root.title("moving object")
can = tk.Canvas(root, height=500, width = 800, bg = "white")
can.pack()
a =[can.create_rectangle(50, 180, 200, 220, fill="red"),
can.create_rectangle(200, 165, 260, 220, fill="darkred"),
can.create_oval(70, 215, 100, 245, fill="black"),
can.create_oval(150, 215, 180, 245, fill="black"),
can.create_oval(210, 215, 240, 245, fill="black")]
can.create_rectangle(0,245,800,500,fill="grey")
def mv():
    for i in a:
      can.move(i,5,0)
    can.after(10,mv)
mv()
root.mainloop()
'''
'''
#moving train
import tkinter as tk
root = tk.Tk()
root.title("moving electric train")
can = tk.Canvas(root, height=500, width=800, bg="white")
can.pack()
a = [
    can.create_oval(-85, 210, -65, 230, fill="black"),
    can.create_oval(-35, 210, -15, 230, fill="black"),
    can.create_oval(-195, 210, -175, 230, fill="black"),
    can.create_oval(-145, 210, -125, 230, fill="black"),
    can.create_oval(-305, 210, -285, 230, fill="black"),
    can.create_oval(-255, 210, -235, 230, fill="black"),
    can.create_oval(-415, 210, -395, 230, fill="black"),
    can.create_oval(-365, 210, -345, 230, fill="black"),
    can.create_rectangle(-100, 170, -10, 220, fill="lightblue", outline="black", width=2),
    can.create_rectangle(-210, 170, -110, 220, fill="cyan", outline="black", width=2),
    can.create_rectangle(-320, 170, -220, 220, fill="yellow", outline="black", width=2),
    can.create_rectangle(-430, 170, -330, 220, fill="lightgreen", outline="black", width=2),
    can.create_rectangle(-110, 190, -100, 200, fill="black"),
    can.create_rectangle(-220, 190, -210, 200, fill="black"),
    can.create_rectangle(-330, 190, -320, 200, fill="black"),
    can.create_line(-55, 170, -55, 140, fill="black", width=3),
]

can.create_line(0, 140, 800, 140, fill="black", width=2)
can.create_rectangle(0, 230, 800, 500, fill="grey")

def mv():
    for i in a:
        can.move(i, 7, 0)
    can.after(10, mv)
mv()

root.mainloop()
'''

#
'''
import tkinter as tk

root = tk.Tk()

can = tk.Canvas(root, height=500, width=800, bg="white")
can.pack()


a = [
    can.create_oval(-85, 210, -65, 230, fill="black"),
    can.create_oval(-35, 210, -15, 230, fill="black"),
    can.create_oval(-195, 210, -175, 230, fill="black"),
    can.create_oval(-145, 210, -125, 230, fill="black"),
    can.create_oval(-305, 210, -285, 230, fill="black"),
    can.create_oval(-255, 210, -235, 230, fill="black"),
    can.create_oval(-415, 210, -395, 230, fill="black"),
    can.create_oval(-365, 210, -345, 230, fill="black"),

    can.create_rectangle(-100, 170, -10, 220, fill="lightblue", outline="black", width=2),
    can.create_rectangle(-210, 170, -110, 220, fill="cyan", outline="black", width=2),
    can.create_rectangle(-320, 170, -220, 220, fill="yellow", outline="black", width=2),
    can.create_rectangle(-430, 170, -330, 220, fill="lightgreen", outline="black", width=2),

    can.create_rectangle(-110, 190, -100, 200, fill="black"),
    can.create_rectangle(-220, 190, -210, 200, fill="black"),
    can.create_rectangle(-330, 190, -320, 200, fill="black"),

    
]

b = [
    can.create_oval(-85, 210, -65, 230, fill="black"),
    can.create_oval(-35, 210, -15, 230, fill="black"),
    can.create_oval(-195, 210, -175, 230, fill="black"),
    can.create_oval(-145, 210, -125, 230, fill="black"),
    can.create_oval(-305, 210, -285, 230, fill="black"),
    can.create_oval(-255, 210, -235, 230, fill="black"),
    can.create_oval(-415, 210, -395, 230, fill="black"),
    can.create_oval(-365, 210, -345, 230, fill="black"),

    can.create_rectangle(-100, 170, -10, 220, fill="pink", outline="black", width=2),
    can.create_rectangle(-210, 170, -110, 220, fill="orange", outline="black", width=2),
    can.create_rectangle(-320, 170, -220, 220, fill="lightgreen", outline="black", width=2),
    can.create_rectangle(-430, 170, -330, 220, fill="darkgreen", outline="black", width=2),

    can.create_rectangle(-110, 190, -100, 200, fill="black"),
    can.create_rectangle(-220, 190, -210, 200, fill="black"),
    can.create_rectangle(-330, 190, -320, 200, fill="black"),

    
]

c = [
    can.create_oval(-85, 210, -65, 230, fill="black"),
    can.create_oval(-35, 210, -15, 230, fill="black"),
    can.create_oval(-195, 210, -175, 230, fill="black"),
    can.create_oval(-145, 210, -125, 230, fill="black"),
    can.create_oval(-305, 210, -285, 230, fill="black"),
    can.create_oval(-255, 210, -235, 230, fill="black"),
    can.create_oval(-415, 210, -395, 230, fill="black"),
    can.create_oval(-365, 210, -345, 230, fill="black"),

    can.create_rectangle(-100, 170, -10, 220, fill="lime", outline="black", width=2),
    can.create_rectangle(-210, 170, -110, 220, fill="black", outline="black", width=2),
    can.create_rectangle(-320, 170, -220, 220, fill="brown", outline="black", width=2),
    can.create_rectangle(-430, 170, -330, 220, fill="peach puff", outline="black", width=2),

    can.create_rectangle(-110, 190, -100, 200, fill="black"),
    can.create_rectangle(-220, 190, -210, 200, fill="black"),
    can.create_rectangle(-330, 190, -320, 200, fill="black"),
   
]

can.create_oval(620, 80, 660, 120, fill="peach puff", outline="black")
can.create_arc(620, 75, 660, 110, start=0, extent=180,fill="red", outline="black")

can.create_oval(630, 95, 634, 99, fill="black")
can.create_oval(646, 95, 650, 99, fill="black")

can.create_arc(632, 100, 648, 110, start=180, extent=180,style="arc", width=2)

can.create_rectangle(635, 120, 645, 128,fill="red",outline="black",width=1)

can.create_rectangle(620, 128, 660, 175, fill="red", outline="black", width=2)

can.create_rectangle(620, 135, 605, 160, width=2,fill="red")#lefthand
can.create_rectangle(660, 135, 675, 160, width=2,fill="red")#righthand


can.create_rectangle(626, 175, 638, 225,fill="red", outline="black")
can.create_rectangle(642, 175, 654, 225, fill="red", outline="black")

can.create_oval(622, 223, 638, 230, fill="gold")
can.create_oval(642, 223, 658, 230, fill="gold")

#tshirt design
can.create_oval(630,135,650,155,fill="cyan")

# Left 
can.create_line(610, 160, 598, 168, width=1)
can.create_line(610, 160, 603, 170, width=1)
can.create_line(610, 160, 607, 172, width=1)
can.create_line(610, 160, 611, 170, width=1)
can.create_line(610, 160, 615, 168, width=1)

# Right 
can.create_line(667, 160, 660, 168, width=1)
can.create_line(667, 160, 665, 170, width=1)
can.create_line(667, 160, 670, 172, width=1)
can.create_line(667, 160, 674, 170, width=1)
can.create_line(667, 160, 679, 168, width=1)
  
def mv():
    for i in a:
        can.move(i, 7, -1)
    can.after(10, mv)
mv()

def m():
    for i in b:
        can.move(i,7, 1)
    can.after(10, m)
m()

def v():
    for i in c:
        can.move(i,7,0)
    can.after(10, v)
v()

root.mainloop()
'''
