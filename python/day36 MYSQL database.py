#
'''
1. Get a particular row by no

For example, to get the row where no = 6:

cursor.execute("SELECT * FROM information WHERE no = %s", (6,))
print(cursor.fetchone())

Output might be:

(6, 'hkdh', 32, 'cse')

fetchone() returns only the first matching row.

2. Get only one particular value

If you only want the name:

cursor.execute("SELECT name FROM information WHERE no = %s", (6,))
print(cursor.fetchone()[0])

Output:

hkdh

Similarly, for age:

cursor.execute("SELECT age FROM information WHERE no = %s", (6,))
print(cursor.fetchone()[0])
3. Search by name
cursor.execute("SELECT * FROM information WHERE name = %s", ('hkdh',))
print(cursor.fetchone())
4. Get multiple matching rows

Use fetchall():

cursor.execute("SELECT * FROM information WHERE department = %s", ('cse',))
print(cursor.fetchall())
Your code with a function

You could make it reusable:

def get_student(no):
    cursor.execute("SELECT * FROM information WHERE no = %s", (no,))
    result = cursor.fetchone()
    print(result)

get_student(6)

Important: (no,) is a tuple containing one value. The comma is required.

Also, using %s parameters like this is the correct approach—don't build SQL by concatenating user input.
'''
#
#
'''
import pymysql as msl
connect = msl.connect(host="localhost",user="root",password="livewire",database="samplee")
cursor = connect.cursor()

#cursor.execute("create table student(sno int, name varchar(20),age int, city varchar(30));")
#cursor.execute("insert into student values(2,'gopi',27,'mayiladuthurai');")
connect.commit()

cursor.execute("select * from student;")
print(cursor.fetchall())
'''
#

#
'''import pymysql as msl
connect = msl.connect(host="localhost",user="root",password="livewire",database="lite")
cursor = connect.cursor()

cursor.execute("create table information(no int,name varchar(30),age int,department varchar(20));")
def imer(a,b,c,d):
    cursor.execute("insert into information values(a,b,c,d);")
imer('1','timer','17','ece')
'''
'''
cursor.execute("insert into information values(2,'nana',17,'CSE');")

cursor.execute("insert into information values(3,'obito',14,'CYBERSECURITY');")

cursor.execute("insert into information values(4,'toji',47,'CIVIL');")
'''
'''
connect.commit()

cursor.execute("select * from information;")
print(cursor.fetchall())'''
#task(sql with function)
'''
import pymysql as msl
connect = msl.connect(host="localhost", user="root", password="livewire", database="lkj")
cursor = connect.cursor()
def create_table(table_name):
    query = f"""CREATE TABLE IF NOT EXISTS {table_name} ( no INT, name VARCHAR(30), age INT, department VARCHAR(20))"""
    cursor.execute(query)
def iler(a, b, c, d, table_name):
    query = f"INSERT INTO {table_name} VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (a, b, c, d))
def update(no, name, age, department, table_name):
    query = f"""UPDATE {table_name} SET name=%s, age=%s, department=%s WHERE no=%s"""
    cursor.execute(query, (name, age, department, no))
def delete(no, table_name):
    query = f"DELETE FROM {table_name} WHERE no=%s"
    cursor.execute(query, (no,))
# Student table
create_table("student")
iler(1, "toji", 47, "cse", "student")
iler(2, "black goku", 100, "god", "student")
update(1, "obito", 14, "legend", "student")
# Teacher table
create_table("teacher")
iler(1, "black goku", 100, "god", "teacher")
iler(2, "toji", 47, "cse", "teacher")
delete(1, "teacher")
connect.commit()
# Display student table
cursor.execute("SELECT * FROM student")
print("student:", cursor.fetchall())
# Display teacher table
cursor.execute("SELECT * FROM teacher")
print("teacher:", cursor.fetchall())
'''
###########
#
'''create database studentmanagement;
use studentmanagement;
create table raylight(student_id int auto_increment primary key,
name varchar(30),phone varchar(30),email varchar(30),
course varchar(30),gender varchar(30),dob varchar(30),
admission varchar(30));
select * from raylight;'''
#
import tkinter as tk
from tkinter import ttk,messagebox
import mysql.connector

def save_student():
    
    name=name_entry.get()
    phone=phone_entry.get()
    email=email_entry.get()
    course=course_box.get()
    gender=gender_box.get()
    dob=dob_entry.get()
    admission=admission_entry.get()

    if name=="" or phone=="" or email=="" or course=="" or gender=="" or dob=="" or admission=="":
        messagebox.showerror("ERROR","fill all the details")
        return
    if not phone.isdigit()or len(phone)!=10:
        messagebox.showerror("ERROR","enter a valid mobile number")
        return
    con=mysql.connector.connect(
        host="localhost",
        user="root",
        password="livewire",
        database="studentmanagement"
        )
    cur=con.cursor()
    
    query="insert into raylight(name,phone,email,course,gender,dob,admission) values(%s,%s,%s,%s,%s,%s,%s)"

    values=(
        name,
        phone,
        email,
        course,
        gender,
        dob,
        admission
        )

    cur.execute(query, values)

        
    con.commit()

    messagebox.showinfo(
            "SUCCESS",
            "Student details saved successfully"
        )

    name_entry.delete(0,tk.END)
    phone_entry.delete(0,tk.END)
    email_entry.delete(0,tk.END)
    course_box.set("")
    gender_box.set("")
    dob_entry.delete(0,tk.END)
    admission_entry.delete(0,tk.END)

    cur.close()
    con.close()

root=tk.Tk()

root.title("student registration")
root.geometry("500x500")

tk.Label(root,text="STUDENT REGISTRATION",bg="lime",fg="black",pady=15).pack(fill="x")

tk.Label(root,text="NAME",font=("Arial",12)).pack()

name_entry=tk.Entry(root,width=35)
name_entry.pack()

tk.Label(root,text="PHONE",font=("Arial",12)).pack()

phone_entry=tk.Entry(root,width=35)
phone_entry.pack()

tk.Label(root,text="EMAIL",font=("Arial",12)).pack()

email_entry=tk.Entry(root,width=35)
email_entry.pack()

tk.Label(root,text="COURSE",font=("Arial",12)).pack()

course_box=ttk.Combobox(root,width=32,state="readonly",values=["python","java","full stack development","artificial intelligence","data science"])
course_box.pack()

tk.Label(root,text="GENDER",font=("Arial",12)).pack()

gender_box=ttk.Combobox(root,width=32,state="readonly",values=["MALE","FEMALE","OTHERS"])
gender_box.pack()

tk.Label(root,text="DOB",font=("Arial",12)).pack()

dob_entry=tk.Entry(root,width=35)
dob_entry.pack()

tk.Label(root,text="ADMISSION",font=("Arial",12)).pack()

admission_entry=tk.Entry(root,width=35)
admission_entry.pack()

tk.Button(root,text="SAVE",command=save_student).pack()

root.mainloop()
