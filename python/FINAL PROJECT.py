#
'''
create database shopping;
use shopping;
CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product VARCHAR(100) NOT NULL,
    price DECIMAL(12,2) NOT NULL,
    customer_name VARCHAR(100) NOT NULL,
    mobile VARCHAR(15) NOT NULL,
    email VARCHAR(150) NOT NULL,
    address TEXT NOT NULL,
    quantity INT NOT NULL,
    total DECIMAL(12,2) NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
SELECT * FROM orders;
'''
#
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector




username = "admin"
password = "1234"




def onlineshopping():

    if n.get() != username or z.get() != password:
        messagebox.showerror(
            "Login Failed",
            "Invalid username or password"
        )
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

    tk.Button(
        k,
        text="Phone",
        command=phone1
    ).grid(row=1, column=0)


    laptop = Image.open(r"D:\NANA\maclaptop.webp")
    laptop = laptop.resize((180, 180))
    laptop_img = ImageTk.PhotoImage(laptop)

    laptop_label = tk.Label(k, image=laptop_img)
    laptop_label.image = laptop_img
    laptop_label.grid(row=0, column=1, padx=20, pady=20)

    tk.Button(
        k,
        text="Laptop",
        command=laptop1
    ).grid(row=1, column=1)


    toycar = Image.open(r"D:\NANA\toycar.webp")
    toycar = toycar.resize((180, 180))
    toycar_img = ImageTk.PhotoImage(toycar)

    toycar_label = tk.Label(k, image=toycar_img)
    toycar_label.image = toycar_img
    toycar_label.grid(row=0, column=2, padx=20, pady=20)

    tk.Button(
        k,
        text="Toy Car",
        command=toycar1
    ).grid(row=1, column=2)


    watch = Image.open(r"D:\NANA\watch.webp")
    watch = watch.resize((180, 180))
    watch_img = ImageTk.PhotoImage(watch)

    watch_label = tk.Label(k, image=watch_img)
    watch_label.image = watch_img
    watch_label.grid(row=0, column=3, padx=20, pady=20)

    tk.Button(
        k,
        text="Watch",
        command=watch1
    ).grid(row=1, column=3)


    k.mainloop()


def order(product, price):

    yt = tk.Toplevel()
    yt.title("Place Order")
    yt.geometry("400x450")


    tk.Label(
        yt,
        text="Product",
        font=("Arial", 12)
    ).pack(pady=5)

    tk.Label(
        yt,
        text=product,
        fg="black"
    ).pack()


    tk.Label(
        yt,
        text="Customer Name"
    ).pack()

    name = tk.Entry(yt, width=25)
    name.pack()


    tk.Label(
        yt,
        text="Mobile"
    ).pack()

    mobile = tk.Entry(yt, width=25)
    mobile.pack()


    tk.Label(
        yt,
        text="Email"
    ).pack()

    email = tk.Entry(yt, width=25)
    email.pack()


    tk.Label(
        yt,
        text="Address"
    ).pack()

    address = tk.Text(
        yt,
        width=25,
        height=3
    )
    address.pack()


    tk.Label(
        yt,
        text="Quantity"
    ).pack()

    qua = tk.Entry(yt, width=25)
    qua.pack()


    tk.Button(
        yt,
        text="PLACE ORDER",
        bg="green",
        fg="white",
        command=lambda: saveorder(
            product,
            price,
            name.get(),
            mobile.get(),
            email.get(),
            address.get("1.0", "end"),
            qua.get()
        )
    ).pack(pady=15)


def saveorder(product, price, name, mobile, email, address, qua):

    if (
        name == ""
        or mobile == ""
        or email == ""
        or qua == ""
        or address.strip() == ""
    ):
        messagebox.showerror(
            "ERROR",
            "Please fill all the information"
        )
        return


    if not mobile.isdigit() or len(mobile) != 10:
        messagebox.showerror(
            "ERROR",
            "Enter a valid mobile number"
        )
        return


    try:

        qua = int(qua)

        if qua <= 0:
            messagebox.showerror(
                "ERROR",
                "Quantity must be greater than 0"
            )
            return


        total = price * qua


        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="livewire",
            database="shopping"
        )


        cursor = db.cursor()

        sql = """
        INSERT INTO orders
        (
            product,
            price,
            customer_name,
            mobile,
            email,
            address,
            quantity,
            total
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """


        values = (
            product,
            price,
            name,
            mobile,
            email,
            address.strip(),
            qua,
            total
        )


        cursor.execute(sql, values)

        db.commit()


        cursor.close()
        db.close()


        messagebox.showinfo(
            "Success",
            "ORDER PLACED SUCCESSFULLY"
        )


    except ValueError:

        messagebox.showerror(
            "ERROR",
            "Quantity must be a number"
        )


    except mysql.connector.Error as e:

        messagebox.showerror(
            "Database Error",
            str(e)
        )


def phone1():

    a = tk.Toplevel()
    a.title("Phones")
    a.geometry("1000x400")


    # PHONE 1

    phones = Image.open(r"D:\NANA\phone1.webp")
    phones = phones.resize((180, 180))
    phones_img = ImageTk.PhotoImage(phones)

    phones_label = tk.Label(a, image=phones_img)
    phones_label.image = phones_img
    phones_label.grid(
        row=0,
        column=0,
        padx=20,
        pady=20
    )


    details = """
Poco X8 Pro
Mediatek 8500
AMOLED Display
6500mAh Battery
₹36,999
"""

    tk.Label(
        a,
        text=details,
        justify="left"
    ).grid(row=1, column=0)


    tk.Button(
        a,
        text="Buy",
        bg="green",
        fg="white",
        command=lambda: order(
            "Poco X8 Pro",
            36999
        )
    ).grid(row=2, column=0, pady=10)


    # PHONE 2

    phones = Image.open(r"D:\NANA\phone2.webp")
    phones = phones.resize((180, 180))
    phones_img = ImageTk.PhotoImage(phones)

    phones_label = tk.Label(a, image=phones_img)
    phones_label.image = phones_img
    phones_label.grid(
        row=0,
        column=1,
        padx=20,
        pady=20
    )


    details = """
Samsung S26 Ultra
12GB RAM
512GB Storage
Snapdragon 8
₹1,47,999
"""

    tk.Label(
        a,
        text=details,
        justify="left"
    ).grid(row=1, column=1)


    tk.Button(
        a,
        text="Buy",
        bg="green",
        fg="white",
        command=lambda: order(
            "Samsung S26 Ultra",
            147999
        )
    ).grid(row=2, column=1, pady=10)


    # PHONE 3

    phones = Image.open(r"D:\NANA\phone3.webp")
    phones = phones.resize((180, 180))
    phones_img = ImageTk.PhotoImage(phones)

    phones_label = tk.Label(a, image=phones_img)
    phones_label.image = phones_img
    phones_label.grid(
        row=0,
        column=2,
        padx=20,
        pady=20
    )


    details = """
IQOO 15
12GB RAM
256GB Storage
LED Display
₹51,999
"""

    tk.Label(
        a,
        text=details,
        justify="left"
    ).grid(row=1, column=2)


    tk.Button(
        a,
        text="Buy",
        bg="green",
        fg="white",
        command=lambda: order(
            "IQOO 15",
            51999
        )
    ).grid(row=2, column=2, pady=10)


    # PHONE 4

    phones = Image.open(r"D:\NANA\phone4.webp")
    phones = phones.resize((180, 180))
    phones_img = ImageTk.PhotoImage(phones)

    phones_label = tk.Label(a, image=phones_img)
    phones_label.image = phones_img
    phones_label.grid(
        row=0,
        column=3,
        padx=20,
        pady=20
    )


    details = """
Vivo T5
6500mAh Battery
6.7 Display
120Hz Refresh
₹34,000
"""

    tk.Label(
        a,
        text=details,
        justify="left"
    ).grid(row=1, column=3)


    tk.Button(
        a,
        text="Buy",
        bg="green",
        fg="white",
        command=lambda: order(
            "Vivo T5",
            34000
        )
    ).grid(row=2, column=3, pady=10)


def laptop1():

    b = tk.Toplevel()
    b.title("Laptops")
    b.geometry("1000x400")


    # LAPTOP 1

    phones = Image.open(r"D:\NANA\laptop1.webp")
    phones = phones.resize((180, 180))
    phones_img = ImageTk.PhotoImage(phones)

    phones_label = tk.Label(b, image=phones_img)
    phones_label.image = phones_img
    phones_label.grid(
        row=0,
        column=0,
        padx=20,
        pady=20
    )


    details = """
ROG Strix
Intel Core i7
14th Gen 14650HX
16GB / 1TB SSD / Windows 11
₹1,60,000
"""

    tk.Label(
        b,
        text=details,
        justify="left"
    ).grid(row=1, column=0)


    tk.Button(
        b,
        text="Buy",
        bg="green",
        fg="white",
        command=lambda: order(
            "ROG Strix",
            160000
        )
    ).grid(row=2, column=0, pady=10)


    # LAPTOP 2

    phones = Image.open(r"D:\NANA\laptop2.webp")
    phones = phones.resize((180, 180))
    phones_img = ImageTk.PhotoImage(phones)

    phones_label = tk.Label(b, image=phones_img)
    phones_label.image = phones_img
    phones_label.grid(
        row=0,
        column=1,
        padx=20,
        pady=20
    )


    details = """
Galaxy Book 4
Intel Core i3
13th Gen 1315U
8GB / 512GB SSD / Windows 11
₹60,000
"""

    tk.Label(
        b,
        text=details,
        justify="left"
    ).grid(row=1, column=1)


    tk.Button(
        b,
        text="Buy",
        bg="green",
        fg="white",
        command=lambda: order(
            "Galaxy Book 4",
            60000
        )
    ).grid(row=2, column=1, pady=10)


    # LAPTOP 3

    phones = Image.open(r"D:\NANA\laptop3.webp")
    phones = phones.resize((180, 180))
    phones_img = ImageTk.PhotoImage(phones)

    phones_label = tk.Label(b, image=phones_img)
    phones_label.image = phones_img
    phones_label.grid(
        row=0,
        column=2,
        padx=20,
        pady=20
    )


    details = """
ASUS Chromebook
Intel Celeron Dual Core
4GB / 64GB EMMC Storage
ChromeOS
₹30,000
"""

    tk.Label(
        b,
        text=details,
        justify="left"
    ).grid(row=1, column=2)


    tk.Button(
        b,
        text="Buy",
        bg="green",
        fg="white",
        command=lambda: order(
            "ASUS Chromebook",
            30000
        )
    ).grid(row=2, column=2, pady=10)


    # LAPTOP 4

    phones = Image.open(r"D:\NANA\laptop4.webp")
    phones = phones.resize((180, 180))
    phones_img = ImageTk.PhotoImage(phones)

    phones_label = tk.Label(b, image=phones_img)
    phones_label.image = phones_img
    phones_label.grid(
        row=0,
        column=3,
        padx=20,
        pady=20
    )


    details = """
HP Laptop
Intel Core i3
13th Gen 1315U
16GB / 512GB SSD / Windows 11
₹50,000
"""

    tk.Label(
        b,
        text=details,
        justify="left"
    ).grid(row=1, column=3)


    tk.Button(
        b,
        text="Buy",
        bg="green",
        fg="white",
        command=lambda: order(
            "HP Laptop",
            50000
        )
    ).grid(row=2, column=3, pady=10)



def toycar1():

    c = tk.Toplevel()
    c.title("Toy Cars")
    c.geometry("1000x400")


    # TOY CAR 1

    phones = Image.open(r"D:\NANA\toycar1.webp")
    phones = phones.resize((180, 180))
    phones_img = ImageTk.PhotoImage(phones)

    phones_label = tk.Label(c, image=phones_img)
    phones_label.image = phones_img
    phones_label.grid(
        row=0,
        column=0,
        padx=20,
        pady=20
    )


    details = """
Bugatti
Top Speed: 300km
Engine: Turbo 5
30 Lakhs
"""

    tk.Label(
        c,
        text=details,
        justify="left"
    ).grid(row=1, column=0)


    tk.Button(
        c,
        text="Buy",
        bg="green",
        fg="white",
        command=lambda: order(
            "Bugatti",
            3000000
        )
    ).grid(row=2, column=0, pady=10)


    # TOY CAR 2

    phones = Image.open(r"D:\NANA\toycar2.webp")
    phones = phones.resize((180, 180))
    phones_img = ImageTk.PhotoImage(phones)

    phones_label = tk.Label(c, image=phones_img)
    phones_label.image = phones_img
    phones_label.grid(
        row=0,
        column=1,
        padx=20,
        pady=20
    )


    details = """
Lamborghini
Engine: Dulex XRT
Top Speed: 400
17 Lakhs
"""

    tk.Label(
        c,
        text=details,
        justify="left"
    ).grid(row=1, column=1)


    tk.Button(
        c,
        text="Buy",
        bg="green",
        fg="white",
        command=lambda: order(
            "Lamborghini",
            1700000
        )
    ).grid(row=2, column=1, pady=10)


    # TOY CAR 3

    phones = Image.open(r"D:\NANA\toycar3.webp")
    phones = phones.resize((180, 180))
    phones_img = ImageTk.PhotoImage(phones)

    phones_label = tk.Label(c, image=phones_img)
    phones_label.image = phones_img
    phones_label.grid(
        row=0,
        column=2,
        padx=20,
        pady=20
    )


    details = """
Hill Climber
Engine: RTX 150
Torque: 120
10 Lakhs
"""

    tk.Label(
        c,
        text=details,
        justify="left"
    ).grid(row=1, column=2)


    tk.Button(
        c,
        text="Buy",
        bg="green",
        fg="white",
        command=lambda: order(
            "Hill Climber",
            1000000
        )
    ).grid(row=2, column=2, pady=10)


    # TOY CAR 4

    phones = Image.open(r"D:\NANA\toycar4.webp")
    phones = phones.resize((180, 180))
    phones_img = ImageTk.PhotoImage(phones)

    phones_label = tk.Label(c, image=phones_img)
    phones_label.image = phones_img
    phones_label.grid(
        row=0,
        column=3,
        padx=20,
        pady=20
    )


    details = """
Destroyer
Engine: Tyro Power
Top Speed: 250
Type: Mudrace
25 Lakhs
"""

    tk.Label(
        c,
        text=details,
        justify="left"
    ).grid(row=1, column=3)


    tk.Button(
        c,
        text="Buy",
        bg="green",
        fg="white",
        command=lambda: order(
            "Destroyer",
            2500000
        )
    ).grid(row=2, column=3, pady=10)



def watch1():

    d = tk.Toplevel()
    d.title("Watches")
    d.geometry("1000x400")


    # WATCH 1

    phones = Image.open(r"D:\NANA\watch.webp")
    phones = phones.resize((180, 180))
    phones_img = ImageTk.PhotoImage(phones)

    phones_label = tk.Label(d, image=phones_img)
    phones_label.image = phones_img
    phones_label.grid(
        row=0,
        column=0,
        padx=20,
        pady=20
    )


    details = """
Casio
Model: AE 1200
Material: Plastic
Price: ₹3,000
"""

    tk.Label(
        d,
        text=details,
        justify="left"
    ).grid(row=1, column=0)


    tk.Button(
        d,
        text="Buy",
        bg="green",
        fg="white",
        command=lambda: order(
            "Casio",
            3000
        )
    ).grid(row=2, column=0, pady=10)


    # WATCH 2

    phones = Image.open(r"D:\NANA\watch1.webp")
    phones = phones.resize((180, 180))
    phones_img = ImageTk.PhotoImage(phones)

    phones_label = tk.Label(d, image=phones_img)
    phones_label.image = phones_img
    phones_label.grid(
        row=0,
        column=1,
        padx=20,
        pady=20
    )


    details = """
Wintage Rex
Model: WD 40
Material: Metal
Price: ₹1,00,000
"""

    tk.Label(
        d,
        text=details,
        justify="left"
    ).grid(row=1, column=1)


    tk.Button(
        d,
        text="Buy",
        bg="green",
        fg="white",
        command=lambda: order(
            "Wintage Rex",
            100000
        )
    ).grid(row=2, column=1, pady=10)


    # WATCH 3

    phones = Image.open(r"D:\NANA\watch2.webp")
    phones = phones.resize((180, 180))
    phones_img = ImageTk.PhotoImage(phones)

    phones_label = tk.Label(d, image=phones_img)
    phones_label.image = phones_img
    phones_label.grid(
        row=0,
        column=2,
        padx=20,
        pady=20
    )


    details = """
Black X
Material: Plastic
Model: Unknown
Price: ₹7,000
"""

    tk.Label(
        d,
        text=details,
        justify="left"
    ).grid(row=1, column=2)


    tk.Button(
        d,
        text="Buy",
        bg="green",
        fg="white",
        command=lambda: order(
            "Black X",
            7000
        )
    ).grid(row=2, column=2, pady=10)


    # WATCH 4

    phones = Image.open(r"D:\NANA\watch3.webp")
    phones = phones.resize((180, 180))
    phones_img = ImageTk.PhotoImage(phones)

    phones_label = tk.Label(d, image=phones_img)
    phones_label.image = phones_img
    phones_label.grid(
        row=0,
        column=3,
        padx=20,
        pady=20
    )


    details = """
Sonata
Material: Plastic
Model: A150
Price: ₹700
"""

    tk.Label(
        d,
        text=details,
        justify="left"
    ).grid(row=1, column=3)


    tk.Button(
        d,
        text="Buy",
        bg="green",
        fg="white",
        command=lambda: order(
            "Sonata",
            700
        )
    ).grid(row=2, column=3, pady=10)


ch = tk.Tk()

ch.title("Project")
ch.geometry("200x180")


tk.Label(
    ch,
    text="User Name:"
).pack(pady=5)

n = tk.Entry(ch)
n.pack()


tk.Label(
    ch,
    text="Password:"
).pack(pady=5)

z = tk.Entry(
    ch,
    show="*"
)
z.pack()


tk.Button(
    ch,
    text="Log In",
    command=onlineshopping
).pack(pady=15)


ch.mainloop()
