#bank application
'''import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
username="a"
password="a"
def openbankdetails():
    if n.get() != username or z.get() != password:
        messagebox.showerror("Login Failed", "Invalid username or password")
        return
    ch.destroy()
    k = tk.Tk()
    k.title("Bank Details")
    tk.Label(k, text="Name:").grid(row=0, column=0)
    name = tk.Entry(k)
    name.grid(row=0, column=1)
    tk.Label(k, text="Email:").grid(row=1, column=0)
    email = tk.Entry(k)
    email.grid(row=1, column=1)
    tk.Label(k, text="A/C Number:").grid(row=2, column=0)
    ac = tk.Entry(k)
    ac.grid(row=2, column=1)
    tk.Label(k, text="Account Type:").grid(row=3, column=0)
    tru = ttk.Combobox(k, values=["Personal", "Joined"], state="readonly")
    tru.current(0)
    tru.grid(row=3, column=1)
    tk.Label(k, text="DOB:").grid(row=4, column=0)
    dob = tk.Entry(k)
    dob.grid(row=4, column=1)
    tk.Label(k, text="Mobile:").grid(row=5, column=0)
    address = tk.Entry(k)
    address.grid(row=5, column=1)
    tk.Label(k, text="Address and Pincode:").grid(row=6, column=0)
    mandp = tk.Text(k, height=2, width=20)
    mandp.grid(row=6, column=1)

    def save():
        f= open("task.txt", "a")
        f.write("\n")
        f.write("Name   : " + name.get() + "\n")
        f.write("Email : " + email.get() + "\n")
        f.write("Account Number : " + ac.get() + "\n")
        f.write("Account Type : " + tru.get() + "\n")
        f.write("DOB : " + dob.get() + "\n")
        f.write("Mobile : " + address.get() + "\n")
        f.write("Address and Pincode :"+mandp.get("1.0", tk.END)+"\n")
        name.delete(0,tk.END)
        email.delete(0,tk.END)
        ac.delete(0,tk.END)
        tru.delete(0,tk.END)
        dob.delete(0,tk.END)
        address.delete(0,tk.END)
        mandp.delete("1.0",tk.END)
        messagebox.showinfo("Success", "Details saved successfully")
    tk.Button(k, text="Submit", command=save).grid(row=7, columnspan=2)
    f.close()
    k.mainloop()
    
ch = tk.Tk()
ch.title("Bank Application")
tk.Label(ch, text="User Name:").pack()
n = tk.Entry(ch)
n.pack()
tk.Label(ch, text="Password:").pack()
z = tk.Entry(ch, show="*")   
z.pack()
tk.Button(ch, text="Log In", command=openbankdetails).pack()
ch.mainloop()'''
#
'''
from PIL import Image, ImageTk

root=tk.Tk()

image=Image.open('spidy.jpg')
image=ImageTk.PhotoImage(image)

image_lable=tk.Label(root, image=image)
image_lable.pack()'''

#project

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

username = "admin"
password = "1234"

def onlineshopping():
    if n.get() != username or z.get() != password:
        messagebox.showerror("Login Failed", "Invalid username or password")
        return
    ch.destroy()
    k = tk.Tk()
    k.title("Online Shopping")
    k.geometry("1000x300")

    phone = Image.open(r"D:\NANA\phone.webp")
    phone = phone.resize((180, 180))
    phone_img = ImageTk.PhotoImage(phone)
    phone_label = tk.Label(k, image=phone_img)
    phone_label.image = phone_img
    phone_label.grid(row=0, column=0, padx=20, pady=20)
    tk.Button(k, text="Phone",command=phone1).grid(row=1, column=0)
#
    laptop = Image.open(r"D:\NANA\maclaptop.webp")
    laptop = laptop.resize((180, 180))
    laptop_img = ImageTk.PhotoImage(laptop)
    laptop_label = tk.Label(k, image=laptop_img)
    laptop_label.image = laptop_img
    laptop_label.grid(row=0, column=1, padx=20, pady=20)
    tk.Button(k, text="Laptop",command=laptop1).grid(row=1, column=1)
#
    laptop = Image.open(r"D:\NANA\toycar.webp")
    laptop = laptop.resize((180, 180))
    laptop_img = ImageTk.PhotoImage(laptop)
    laptop_label = tk.Label(k, image=laptop_img)
    laptop_label.image = laptop_img
    laptop_label.grid(row=0, column=2, padx=20, pady=20)
    tk.Button(k, text="toycar",command=toycar1).grid(row=1, column=2)
#
    laptop = Image.open(r"D:\NANA\watch.webp")
    laptop = laptop.resize((180, 180))
    laptop_img = ImageTk.PhotoImage(laptop)
    laptop_label = tk.Label(k, image=laptop_img)
    laptop_label.image = laptop_img
    laptop_label.grid(row=0, column=3, padx=20, pady=20)
    tk.Button(k, text="watch",command=watch1).grid(row=1, column=3)

    k.mainloop()

def order(product,price):
    yt=tk.Toplevel()
    yt.title("place order")
    yt.geometry("400x450")

    tk.Label(yt,text="product",font=("Arial",12)).pack(pady=5)
    tk.Label(yt,text=product,fg="black").pack()


    tk.Label(yt,text="Customer name").pack()
    name=tk.Entry(yt,width=25)
    name.pack()

    tk.Label(yt,text="Mobile").pack()
    mobile=tk.Entry(yt,width=25)
    mobile.pack()

    tk.Label(yt,text="Email").pack()
    email=tk.Entry(yt,width=25)
    email.pack()

    tk.Label(yt,text="Address").pack()
    address=tk.Text(yt,width=25,height=3)
    address.pack()

    tk.Label(yt,text="Quantity").pack()
    qua=tk.Entry(yt,width=25)
    qua.pack()

    tk.Button(yt,text="PLACE ORDER",bg="green",fg="white",command=lambda:saveorder(product,price,name.get(),mobile.get(),email.get(),address.get("1.0","end"),qua.get())).pack(pady=15)

def saveorder(product,price,name,mobile,email,address,qua):
    if name==""or mobile==""or email==""or qua=="" or address=="":
        messagebox.showerror("ERROR","please fill all the information")
        return
    if not mobile.isdigit()or len(mobile)!=10:
        messagebox.showerror("ERROR","enter a valid mobile number")
        return
    qua=int(qua)
    total=price*qua
    f=open("task.txt","a")

    f.write("=================\n")
    f.write(f"PRODUCT: {product}\n")
    f.write(f"NAME: {name}\n")
    f.write(f"MOBILE: {mobile}\n")
    f.write(f"EMAIL: {email}\n")
    f.write(f"ADDRESS: {address.strip()}\n")
    f.write(f"QUANTITY: {qua}\n")
    f.write(f"TOTAL: {total}\n")
    f.write("=================\n")

    messagebox.showinfo("over","ORDER PLACED SUCCESSFULLY")

    
def phone1():
    a = tk.Toplevel()
    a.title("Phones")
    a.geometry("1000x400")
    
    phones = Image.open(r"D:\NANA\phone1.webp")
    phones = phones.resize((180, 180))
    phones_img = ImageTk.PhotoImage(phones)
    phones_label = tk.Label(a, image=phones_img)   
    phones_label.image = phones_img                
    phones_label.grid(row=0, column=0, padx=20, pady=20)
    details="""
    poco x8 pro
    mediatech 8500
    amoled display
    6500mah battery
    ₹36,999"""
    price=36999
    tk.Label(a,text=details,justify="left").grid(row=1,column=0)

    tk.Button(a,text="Buy",bg="green",fg="white",command=lambda:order("poco X8",36999)).grid(row=2,column=0,pady=10)
    #
    phones = Image.open(r"D:\NANA\phone2.webp")
    phones = phones.resize((180, 180))
    phones_img = ImageTk.PhotoImage(phones)
    phones_label = tk.Label(a, image=phones_img)   
    phones_label.image = phones_img                
    phones_label.grid(row=0, column=1, padx=20, pady=20)
    details="""
    samsung S26 ultra
    12gb ram
    512gb storage
    snapdragon 8
    ₹1,47,999"""
    tk.Label(a,text=details,justify="left").grid(row=1,column=1)

    tk.Button(a,text="Buy",bg="green",fg="white",command=lambda:order("samsung s26",47999)).grid(row=2,column=1,pady=10)
    
    #
    phones = Image.open(r"D:\NANA\phone3.webp")
    phones = phones.resize((180, 180))
    phones_img = ImageTk.PhotoImage(phones)
    phones_label = tk.Label(a, image=phones_img)   
    phones_label.image = phones_img                
    phones_label.grid(row=0, column=2, padx=20, pady=20)
    details="""
    iqoo 15
    12gb ram
    256gb storage
    led display
    ₹51,999"""
    tk.Label(a,text=details,justify="left").grid(row=1,column=2)

    tk.Button(a,text="Buy",bg="green",fg="white",command=lambda:order("IQOO 15",51999)).grid(row=2,column=2,pady=10)
    
    #
    phones = Image.open(r"D:\NANA\phone4.webp")
    phones = phones.resize((180, 180))
    phones_img = ImageTk.PhotoImage(phones)
    phones_label = tk.Label(a, image=phones_img)   
    phones_label.image = phones_img                
    phones_label.grid(row=0, column=3, padx=20, pady=20)
    details="""
    vivo T5
    6500mah battery
    6.7' display
    120hz refresh
    ₹34,000"""
    tk.Label(a,text=details,justify="left").grid(row=1,column=3)

    tk.Button(a,text="Buy",bg="green",fg="white",command=lambda:order("vivo T5",34000)).grid(row=2,column=3,pady=10)
    
    a.mainloop()
#
def laptop1():
    b = tk.Toplevel()
    b.title("laptops")
    b.geometry("1000x400")
    
    phones = Image.open(r"D:\NANA\laptop1.webp")
    phones = phones.resize((180, 180))
    phones_img = ImageTk.PhotoImage(phones)
    phones_label = tk.Label(b, image=phones_img)   
    phones_label.image = phones_img                
    phones_label.grid(row=0, column=0, padx=20, pady=20)
    details="""
    rog strix
    Intel Core i7
    14th Gen 14650HX
    16 GB/1 TB SSD/Windows11
    ₹1,60,000"""
    tk.Label(b,text=details,justify="left").grid(row=1,column=0)

    tk.Button(b,text="Buy",bg="green",fg="white",command=lambda:order("rog strix",160000)).grid(row=2,column=0,pady=10)
    
    #
    phones = Image.open(r"D:\NANA\laptop2.webp")
    phones = phones.resize((180, 180))
    phones_img = ImageTk.PhotoImage(phones)
    phones_label = tk.Label(b, image=phones_img)   
    phones_label.image = phones_img                
    phones_label.grid(row=0, column=1, padx=20, pady=20)
    details="""
    galaxy book 4
    Intel Core i3
    13th Gen 1315U
    8GB512GBSSDWindows11
    ₹60,000"""
    tk.Label(b,text=details,justify="left").grid(row=1,column=1)

    tk.Button(b,text="Buy",bg="green",fg="white",command=lambda:order("galaxy book 4",60000)).grid(row=2,column=1,pady=10)
    
    #
    phones = Image.open(r"D:\NANA\laptop3.webp")
    phones = phones.resize((180, 180))
    phones_img = ImageTk.PhotoImage(phones)
    phones_label = tk.Label(b, image=phones_img)   
    phones_label.image = phones_img                
    phones_label.grid(row=0, column=2, padx=20, pady=20)
    details="""
    ASUS CHROMEBOOK
    IntelCeleronDualCoreN50
    4GB64GBEMMCStorageChromeOS
    CX1505CTA-S70256
    ₹30,000"""
    tk.Label(b,text=details,justify="left").grid(row=1,column=2)

    tk.Button(b,text="Buy",bg="green",fg="white",command=lambda:order("ASUS",30000)).grid(row=2,column=2,pady=10)
    
    #
    phones = Image.open(r"D:\NANA\laptop4.webp")
    phones = phones.resize((180, 180))
    phones_img = ImageTk.PhotoImage(phones)
    phones_label = tk.Label(b, image=phones_img)   
    phones_label.image = phones_img                
    phones_label.grid(row=0, column=3, padx=20, pady=20)
    details="""
    hp laptop
    IntelCorei3
    13th Gen 1315U
    16GB512GBSSDWindows11
    ₹50,000"""
    tk.Label(b,text=details,justify="left").grid(row=1,column=3)

    tk.Button(b,text="Buy",bg="green",fg="white",command=lambda:order("hp",50000)).grid(row=2,column=3,pady=10)
    
    b.mainloop()
#
def toycar1():
    c = tk.Toplevel()
    c.title("laptops")
    c.geometry("1000x400")
    
    phones = Image.open(r"D:\NANA\toycar1.webp")
    phones = phones.resize((180, 180))
    phones_img = ImageTk.PhotoImage(phones)
    phones_label = tk.Label(c, image=phones_img)   
    phones_label.image = phones_img                
    phones_label.grid(row=0, column=0, padx=20, pady=20)
    details="""
    Bugatti
    topspeed:300km
    engine:turbo 5
    30 lakhs"""
    tk.Label(c,text=details,justify="left").grid(row=1,column=0)

    tk.Button(c,text="Buy",bg="green",fg="white",command=lambda:order("Bugatti",3)).grid(row=2,column=0,pady=10)
    
    #
    phones = Image.open(r"D:\NANA\toycar2.webp")
    phones = phones.resize((180, 180))
    phones_img = ImageTk.PhotoImage(phones)
    phones_label = tk.Label(c, image=phones_img)   
    phones_label.image = phones_img                
    phones_label.grid(row=0, column=1, padx=20, pady=20)
    details="""
    lamborghini
    engine:dulex xrt
    topspeed:400
    17 lakhs"""
    tk.Label(c,text=details,justify="left").grid(row=1,column=1)

    tk.Button(c,text="Buy",bg="green",fg="white",command=lambda:order("Lamborghini")).grid(row=2,column=1,pady=10)
    
    #
    phones = Image.open(r"D:\NANA\toycar3.webp")
    phones = phones.resize((180, 180))
    phones_img = ImageTk.PhotoImage(phones)
    phones_label = tk.Label(c, image=phones_img)   
    phones_label.image = phones_img                
    phones_label.grid(row=0, column=2, padx=20, pady=20)
    details="""
    hill climber
    engine:rtx 150
    torque:120
    10 lakhs"""
    tk.Label(c,text=details,justify="left").grid(row=1,column=2)

    tk.Button(c,text="Buy",bg="green",fg="white",command=lambda:order("Hill Climber")).grid(row=2,column=2,pady=10)
    
    #
    phones = Image.open(r"D:\NANA\toycar4.webp")
    phones = phones.resize((180, 180))
    phones_img = ImageTk.PhotoImage(phones)
    phones_label = tk.Label(c, image=phones_img)   
    phones_label.image = phones_img                
    phones_label.grid(row=0, column=3, padx=20, pady=20)
    details="""
    Destroyer
    engine:tyro power
    top speed:250
    type:mudrace
    25 lakhs
    """
    tk.Label(c,text=details,justify="left").grid(row=1,column=3)

    tk.Button(c,text="Buy",bg="green",fg="white",command=lambda:order("Destroyer")).grid(row=2,column=3,pady=10)
    
    c.mainloop()
#
def watch1():
    d = tk.Toplevel()
    d.title("laptops")
    d.geometry("1000x400")
    
    phones = Image.open(r"D:\NANA\watch.webp")
    phones = phones.resize((180, 180))
    phones_img = ImageTk.PhotoImage(phones)
    phones_label = tk.Label(d, image=phones_img)   
    phones_label.image = phones_img                
    phones_label.grid(row=0, column=0, padx=20, pady=20)
    details="""
    casio
    model:AE 1200
    material:plastic
    price:₹3000"""
    tk.Label(d,text=details,justify="left").grid(row=1,column=0)

    tk.Button(d,text="Buy",bg="green",fg="white",command=lambda:order("casio")).grid(row=2,column=0,pady=10)
    
    #
    phones = Image.open(r"D:\NANA\watch1.webp")
    phones = phones.resize((180, 180))
    phones_img = ImageTk.PhotoImage(phones)
    phones_label = tk.Label(d, image=phones_img)   
    phones_label.image = phones_img                
    phones_label.grid(row=0, column=1, padx=20, pady=20)
    details="""
    wintage rex
    model:wd 40
    material:metal
    price:₹1,00,000"""
    tk.Label(d,text=details,justify="left").grid(row=1,column=1)

    tk.Button(d,text="Buy",bg="green",fg="white",command=lambda:order("wintage")).grid(row=2,column=1,pady=10)
    
    #
    phones = Image.open(r"D:\NANA\watch2.webp")
    phones = phones.resize((180, 180))
    phones_img = ImageTk.PhotoImage(phones)
    phones_label = tk.Label(d, image=phones_img)   
    phones_label.image = phones_img                
    phones_label.grid(row=0, column=2, padx=20, pady=20)
    details="""
    black x
    material:plastic
    model:unknown
    price:₹7000"""
    tk.Label(d,text=details,justify="left").grid(row=1,column=2)

    tk.Button(d,text="Buy",bg="green",fg="white",command=lambda:order("black x")).grid(row=2,column=2,pady=10)
    
    #
    phones = Image.open(r"D:\NANA\watch3.webp")
    phones = phones.resize((180, 180))
    phones_img = ImageTk.PhotoImage(phones)
    phones_label = tk.Label(d, image=phones_img)   
    phones_label.image = phones_img                
    phones_label.grid(row=0, column=3, padx=20, pady=20)
    details="""
    sonata
    material:plastic
    model:a150
    price:₹700"""
    tk.Label(d,text=details,justify="left").grid(row=1,column=3)

    tk.Button(d,text="Buy",bg="green",fg="white",command=lambda:order("sonata")).grid(row=2,column=3,pady=10)
    
    d.mainloop()
    
ch = tk.Tk()
ch.title("Project")
ch.geometry("200x180")
tk.Label(ch, text="User Name:").pack(pady=5)
n = tk.Entry(ch)
n.pack()
tk.Label(ch, text="Password:").pack(pady=5)
z = tk.Entry(ch, show="*")
z.pack()
tk.Button(ch, text="Log In", command=onlineshopping).pack(pady=15)
ch.mainloop()

