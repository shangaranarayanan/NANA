#gui(tkinter)
import tkinter as tk
'''
ch=tk.Tk()
ch.title("creating")
ch.mainloop()

#label(Label)
ch=tk.Tk()
tk.Label(ch,text="universe 7").pack()
tk.Label(ch,text="vs").pack()
tk.Label(ch,text="universe 11").pack()
ch.mainloop()

#entry and text
ch=tk.Tk()
n=tk.Entry(ch)
n.pack()
k=tk.Entry()
k.pack()
s=tk.Text(ch,height=4,width=12)
s.pack()
ch.mainloop()

#button
ch=tk.Tk()
click1=tk.Button(ch,text="open")
click1.pack()
click2=tk.Button(ch,text="close",command=ch.destroy)
click2.pack()
ch.mainloop()

#
ch=tk.Tk()
ch.title("Tournament Of Power")
tk.Label(ch,text="task").pack()
n=tk.Entry(ch)
n.pack()
k=tk.Entry()
k.pack()
s=tk.Text(ch,height=2,width=14)
s.pack()
n=tk.Entry()
n.pack()
ch.mainloop()
'''
'''
########
ch=tk.Tk()
ch.title("biometric form")
name=tk.Label(ch,text="Name:")
name.grid(row=0,column=0)
n1 = tk.Entry(ch)
n1.grid(row=0,column=1)


age=tk.Label(ch,text="Age:")
age.grid(row=1,column=0)
k1 = tk.Entry(ch)
k1.grid(row=1,column=1)

year=tk.Label(ch,text="DOB:")
year.grid(row=2,column=0)
z1 = tk.Entry(ch)
z1.grid(row=2,column=1)

place=tk.Label(ch,text="Place:")
place.grid(row=3,column=0)
s1 = tk.Entry(ch)
s1.grid(row=3,column=1)

btn = tk.Button(ch, text="submit",command=ch.destroy)
btn.grid(row=4,columnspan=2)

ch.mainloop()
'''
'''
#radio
ch= tk.Tk()

game = tk.IntVar()
game1 = tk.Radiobutton(ch, variable=game, value=0, text="FF")
game2 = tk.Radiobutton(ch, variable=game, value=1, text="BGMI")
game1.pack()
game2.pack()

ch.mainloop()

#check
ch= tk.Tk()

game2 = tk.IntVar()
game3 = tk.IntVar()
game1 = tk.Checkbutton(ch, variable=game2, text="FF")
game2 = tk.Checkbutton(ch, variable=game3, text="BGMI")
game1.pack()
game2.pack()

ch.mainloop()
'''
#'
'''
ch= tk.Tk()

game2 = tk.IntVar()
game3 = tk.IntVar()
game1 = tk.Checkbutton(ch, variable=game2, text="FF")
game2 = tk.Checkbutton(ch, variable=game3, text="BGMI")
game1.grid(row=1,column=0)
game2.grid(row=1,column=2)

ch.mainloop()
#'
ch= tk.Tk()

game = tk.IntVar()
game1 = tk.Radiobutton(ch, variable=game, value=0, text="goku")
game2 = tk.Radiobutton(ch, variable=game, value=1, text="goku black")
game1.grid(row=0,column=0)
game2.grid(row=1,column=0)

ch.mainloop()
'''
'''
#combo box
import tkinter as tk
from tkinter import ttk

def select(event):
    selecteditem = combobox.get()
    label.config(text="Selected Item: " + selecteditem)

root = tk.Tk()
root.title("Combobox Example")

label = tk.Label(root, text="Selected Item: ")
label.pack()

combobox = ttk.Combobox(root, values=["type 1", "type 2", "type3"], state='readonly')
combobox.pack()

combobox.set("type2")

combobox.bind("<<ComboboxSelected>>", select)
root.mainloop()
#message box(showwarning)(showwarning)
from tkinter import messagebox
root = tk.Tk()
root.title("message box")

def send():
    data = entry.get()
    messagebox.showwarning('message','the message is\n'+data)

label = tk.Label(root, text="enter the message")
label.grid(row=0)

entry = tk.Entry(root)
entry.grid(row=0,column=1)

bt = tk.Button(root, text="msg", command=send)
bt.grid(row=1, columnspan=2)

root.mainloop()
'''
'''
#task
import tkinter as tk
from tkinter import ttk
ch=tk.Tk()
game = tk.IntVar()
ch.title("biometric form")
name=tk.Label(ch,text="Name:")
name.grid(row=0,column=0)
n1 = tk.Entry(ch)
n1.grid(row=0,column=1)

age=tk.Label(ch,text="email:")
age.grid(row=1,column=0)
k1 = tk.Entry(ch)
k1.grid(row=1,column=1)

year=tk.Label(ch,text="room type:")
year.grid(row=2,column=0)
combo_box = ttk.Combobox(ch, values=["economy", "business","normal"], state='readonly')
combo_box.set("normal")
combo_box.grid(row=2,column=1)

place=tk.Label(ch,text="arrival date:")
place.grid(row=3,column=0)
s1 = tk.Entry(ch)
s1.grid(row=3,column=1)

meny=tk.Label(ch,text="depature date:")
meny.grid(row=4,column=0)
y1 = tk.Entry(ch)
y1.grid(row=4,column=1)

zeny=tk.Label(ch,text="no of guest:")
zeny.grid(row=5,column=0)
r1 = tk.Entry(ch)
r1.grid(row=5,column=1)

me=tk.Label(ch,text="free pickup:")
me.grid(row=6,column=0)

game1 = tk.Radiobutton(ch, variable=game, value=0, text="yes")
game2 = tk.Radiobutton(ch, variable=game, value=1, text="no")
game1.grid(row=6,column=1)
game2.grid(row=6,column=2)

ny=tk.Label(ch,text="flight number:")
ny.grid(row=7,column=0)
o1 = tk.Entry(ch)
o1.grid(row=7,column=1)

zo=tk.Label(ch,text="special request:")
zo.grid(row=8,column=0)
g1 = tk.Entry(ch)
g1.grid(row=8,column=1)

button2 = tk.Button(ch, text="submit", command=ch.destroy)
button2.grid(row=10,columnspan=3)

ch.mainloop()
'''
#
'''
import tkinter as tk
ch=tk.Tk()
game = tk.IntVar()
name=tk.Label(ch,text="Name:")
name.place(x=10,y=10)
n1 = tk.Entry(ch)
n1.place(x=60,y=10)

me=tk.Label(ch,text="gender:")
me.place(x=10,y=40)

game1 = tk.Radiobutton(ch, variable=game, value=0, text="male")
game2 = tk.Radiobutton(ch, variable=game, value=1, text="female")
game1.place(x=60,y=40)
game2.place(x=120,y=40)
#
# PIL
import tkinter as tk
from PIL import Image, ImageTk

root=tk.Tk()

image=Image.open('spidy.jpg')
image=ImageTk.PhotoImage(image)

image_lable=tk.Label(root, image=image)
image_lable.pack()

root.mainloop()
'''
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
username="admin"
password="1234"
def openbankdetails():
    if n.get()!=username or z.get()!=password:
        messagebox.showerror("login failed","invalid username or password")
        return
    ch.destroy()   
    k = tk.Tk()
    k.title("Bank Details")
    tk.Label(k, text="Name:").grid(row=0, column=0)
    name=tk.Entry(k).grid(row=0, column=1)
    tk.Label(k, text="Email:").grid(row=1, column=0)
    email=tk.Entry(k).grid(row=1, column=1)
    tk.Label(k, text="A/C Number:").grid(row=2, column=0)
    ac=tk.Entry(k).grid(row=2, column=1)
    tk.Label(k, text="Account Type:").grid(row=3, column=0)
    tru = ttk.Combobox(k, values=["Personal", "Joined"], state="readonly")
    tru.current(0)
    tru.grid(row=3, column=1)
    tk.Label(k, text="DOB:").grid(row=4, column=0)
    dob=tk.Entry(k).grid(row=4, column=1)
    tk.Label(k, text="Address:").grid(row=5, column=0)
    address=tk.Entry(k).grid(row=5, column=1)
    tk.Label(k, text="Mobile No and Pincode:").grid(row=6, column=0)
    mandp=tk.Text(k, height=2, width=20).grid(row=6, column=1)
    tk.Button(k, text="Submit", command=k.destroy).grid(row=7, columnspan=2)
    k.mainloop()
def save():
    f=open("task2.txt","w")
    f.write("Name:"+name.get()+"\n")
    file.close()
# Login window
ch = tk.Tk()
ch.title("Bank Application")
tk.Label(ch, text="User Name:").pack()
n = tk.Entry(ch)
n.pack()
tk.Label(ch, text="Password:").pack()
z = tk.Entry(ch, show="*")   
z.pack()
tk.Button(ch, text="Log In", command=openbankdetails).pack()
ch.mainloop()
