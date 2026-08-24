
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import re

def db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="livewire",   
        database="student_management"
    )

def clear():
    for box in [student_id, name, phone, email, dob, admission]:
        box.delete(0, tk.END)

    course.set("")
    gender.set("")

def valid():
    if not all([
        name.get(), phone.get(), email.get(),
        course.get(), gender.get(),
        dob.get(), admission.get()
    ]):
        messagebox.showwarning("Error", "Please fill all fields")
        return False

    if not phone.get().isdigit() or len(phone.get()) != 10:
        messagebox.showwarning(
            "Error",
            "Phone number must contain 10 digits"
        )
        return False

    if not re.match(r"^[\w.-]+@[\w.-]+\.\w+$", email.get()):
        messagebox.showwarning(
            "Error",
            "Please enter a valid email"
        )
        return False

    return True

def view():
    table.delete(*table.get_children())

    try:
        con = db()
        cur = con.cursor()

        cur.execute("SELECT * FROM students")

        for row in cur.fetchall():
            table.insert("", tk.END, values=row)

        con.close()

    except Exception as e:
        messagebox.showerror("Database Error", str(e))

def add():
    if not valid():
        return

    try:
        con = db()
        cur = con.cursor()

        query = """
        INSERT INTO students
        (name, phone, email, course, gender,
         date_of_birth, admission_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            name.get(),
            phone.get(),
            email.get(),
            course.get(),
            gender.get(),
            dob.get(),
            admission.get()
        )

        cur.execute(query, values)
        con.commit()
        con.close()

        messagebox.showinfo(
            "Success",
            "Student added successfully"
        )

        clear()
        view()

    except Exception as e:
        messagebox.showerror("Database Error", str(e))

def search_student():
    value = search.get().strip()

    if not value:
        messagebox.showwarning(
            "Search",
            "Enter Student ID or Name"
        )
        return

    table.delete(*table.get_children())

    try:
        con = db()
        cur = con.cursor()

        if value.isdigit():
            cur.execute(
                "SELECT * FROM students WHERE student_id=%s",
                (value,)
            )
        else:
            cur.execute(
                "SELECT * FROM students WHERE name LIKE %s",
                ("%" + value + "%",)
            )

        rows = cur.fetchall()

        for row in rows:
            table.insert("", tk.END, values=row)

        con.close()

        if not rows:
            messagebox.showinfo(
                "Search",
                "Student not found"
            )

    except Exception as e:
        messagebox.showerror("Database Error", str(e))

def select_student(event):
    selected = table.focus()

    if not selected:
        return

    data = table.item(selected)["values"]

    clear()

    student_id.insert(0, data[0])
    name.insert(0, data[1])
    phone.insert(0, data[2])
    email.insert(0, data[3])

    course.set(data[4])
    gender.set(data[5])

    dob.insert(0, data[6])
    admission.insert(0, data[7])
    
def update():
    if not student_id.get():
        messagebox.showwarning(
            "Error",
            "Select a student first"
        )
        return

    if not valid():
        return

    try:
        con = db()
        cur = con.cursor()

        query = """
        UPDATE students SET
        name=%s,
        phone=%s,
        email=%s,
        course=%s,
        gender=%s,
        date_of_birth=%s,
        admission_date=%s
        WHERE student_id=%s
        """
        values = (
            name.get(),
            phone.get(),
            email.get(),
            course.get(),
            gender.get(),
            dob.get(),
            admission.get(),
            student_id.get()
        )

        cur.execute(query, values)
        con.commit()

        if cur.rowcount == 0:
            messagebox.showinfo(
                "Update",
                "Student not found"
            )
        else:
            messagebox.showinfo(
                "Success",
                "Student updated successfully"
            )

        con.close()
        view()

    except Exception as e:
        messagebox.showerror("Database Error", str(e))
def delete():
    if not student_id.get():
        messagebox.showwarning(
            "Error",
            "Select a student first"
        )
        return

    answer = messagebox.askyesno(
        "Delete",
        "Are you sure you want to delete this student?"
    )

    if not answer:
        return

    try:
        con = db()
        cur = con.cursor()

        cur.execute(
            "DELETE FROM students WHERE student_id=%s",
            (student_id.get(),)
        )

        con.commit()

        if cur.rowcount == 0:
            messagebox.showinfo(
                "Delete",
                "Student not found"
            )
        else:
            messagebox.showinfo(
                "Success",
                "Student deleted successfully"
            )

        con.close()

        clear()
        view()
        
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
root = tk.Tk()
root.title("Student Management System")
root.geometry("1100x650")
root.configure(bg="#f2f2f2")
title = tk.Label(
    root,
    text="STUDENT MANAGEMENT SYSTEM",
    font=("Arial", 20, "bold"),
    bg="#1f4e78",
    fg="white",
    pady=15
)
title.pack(fill="x")
input_frame = tk.Frame(
    root,
    bg="#f2f2f2"
)
input_frame.pack(pady=15)

labels = [
    "Student ID",
    "Name",
    "Phone",
    "Email",
    "Course",
    "Gender",
    "Date of Birth",
    "Admission Date"
]
for i, text in enumerate(labels):
    tk.Label(
        input_frame,
        text=text,
        font=("Arial", 10, "bold"),
        bg="#f2f2f2"
    ).grid(
        row=i,
        column=0,
        padx=10,
        pady=5,
        sticky="w"
    )

student_id = tk.Entry(input_frame, width=30)
name = tk.Entry(input_frame, width=30)
phone = tk.Entry(input_frame, width=30)
email = tk.Entry(input_frame, width=30)
dob = tk.Entry(input_frame, width=30)
admission = tk.Entry(input_frame, width=30)

student_id.grid(row=0, column=1, pady=5)
name.grid(row=1, column=1, pady=5)
phone.grid(row=2, column=1, pady=5)
email.grid(row=3, column=1, pady=5)
dob.grid(row=6, column=1, pady=5)
admission.grid(row=7, column=1, pady=5)
course = ttk.Combobox(
    input_frame,
    width=27,
    state="readonly",
    values=[
        "Python",
        "Java",
        "Data Science",
        "Artificial Intelligence",
        "Full Stack Development"
    ]
)
course.grid(row=4, column=1, pady=5)
gender = ttk.Combobox(
    input_frame,
    width=27,
    state="readonly",
    values=[
        "Male",
        "Female",
        "Other"
    ]
)
gender.grid(row=5, column=1, pady=5)
button_frame = tk.Frame(
    root,
    bg="#f2f2f2"
)
button_frame.pack(pady=10)
tk.Button(
    button_frame,
    text="Add",
    width=12,
    command=add
).grid(row=0, column=0, padx=5)
tk.Button(
    button_frame,
    text="Update",
    width=12,
    command=update
).grid(row=0, column=1, padx=5)
tk.Button(
    button_frame,
    text="Delete",
    width=12,
    command=delete
).grid(row=0, column=2, padx=5)
tk.Button(
    button_frame,
    text="View",
    width=12,
    command=view
).grid(row=0, column=3, padx=5)
tk.Button(
    button_frame,
    text="Clear",
    width=12,
    command=clear
).grid(row=0, column=4, padx=5)

search_frame = tk.Frame(
    root,
    bg="#f2f2f2"
)
search_frame.pack(pady=5)
tk.Label(
    search_frame,
    text="Search ID / Name:",
    font=("Arial", 10, "bold"),
    bg="#f2f2f2"
).pack(side="left")
search = tk.Entry(
    search_frame,
    width=25
)
search.pack(
    side="left",
    padx=10
)
tk.Button(
    search_frame,
    text="Search",
    command=search_student
).pack(side="left")
columns = (
    "ID",
    "Name",
    "Phone",
    "Email",
    "Course",
    "Gender",
    "DOB",
    "Admission"
)
table = ttk.Treeview(
    root,
    columns=columns,
    show="headings"
)
for column in columns:
    table.heading(
        column,
        text=column
    )
    table.column(
        column,
        width=130
    )
table.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)
table.bind(
    "<ButtonRelease-1>",
    select_student
)
view()
root.mainloop()
