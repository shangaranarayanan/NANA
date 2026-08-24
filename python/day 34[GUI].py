#bank application(task)
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
        f.write("Address and Pincode :"+mandp.get("1.0", tk.END)+"\n")r
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
ch.mainloop()
'''

#speech recognition(model ex)
'''
import tkinter as tk
import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="Listening...")
        window.update()
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            result_text.set(text)
            status_label.config(text="Recognition complete.")
        except sr.UnknownValueError:
            result_text.set("Could not understand audio.")
            status_label.config(text="Try again.")
        except sr.RequestError:
            
            result_text.set("API unavailable.")
            status_label.config(text="Error.")

# GUI setup
window = tk.Tk()
window.title("Speech Recognition App")
window.geometry("400x200")

result_text = tk.StringVar()

tk.Label(window, text="Click to Speak", font=("Arial", 14)).pack(pady=10)
tk.Button(window, text="Start Listening", command=recognize_speech).pack(pady=10)
tk.Label(window, textvariable=result_text, wraplength=350, font=("Arial", 12)).pack(pady=10)
status_label = tk.Label(window, text="", font=("Arial", 10), fg="blue")
status_label.pack()

window.mainloop()
'''
'''
#speech recognition(smaller version)
import tkinter as tk
import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            text.set(r.recognize_google(r.listen(source)))
        except:
            text.set("Could not recognize")

root = tk.Tk()
root.title("Speech App")

text = tk.StringVar()

tk.Button(root, text="Speak", command=listen).pack(pady=10)
tk.Label(root, textvariable=text).pack(pady=10)

root.mainloop()
'''
'''
#speech recognition
import tkinter as tk
import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="Listening...")
        window.update()
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            result_text.set(text)
            status_label.config(text="Recognition complete.")
        except sr.UnknownValueError:
            result_text.set("Could not understand audio.")
            status_label.config(text="Try again.")
        except sr.RequestError:
            
            result_text.set("API unavailable.")
            status_label.config(text="Error.")

window = tk.Tk()
window.title("Speech Recognition App")
window.geometry("400x200")

result_text = tk.StringVar()

tk.Label(window, text="Click to Speak", font=("Arial", 14)).pack(pady=10)
tk.Button(window, text="Start Listening", command=recognize_speech).pack(pady=10)
tk.Label(window, textvariable=result_text, wraplength=350, font=("Arial", 12)).pack(pady=10)
status_label = tk.Label(window, text="", font=("Arial", 10), fg="blue")
status_label.pack()

window.mainloop()
'''
'''
#QR code generator
import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    data = entry.get()
    if not data:
        messagebox.showwarning("Input Error", "Please enter some text to generate QR code.")
        return

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img = img.resize((200, 200))  # Resize for display

    img_tk = ImageTk.PhotoImage(img)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk  # Keep reference to avoid garbage collection

# GUI setup
root = tk.Tk()
root.title("QR Code Generator")

tk.Label(root, text="Enter text or URL:").pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

tk.Button(root, text="Generate QR Code", command=generate_qr).pack(pady=10)

qr_label = tk.Label(root)
qr_label.pack(pady=10)

root.mainloop()
'''
'''
#QR CODE GENERATOR(smaller version)
#https://maps.app.goo.gl/gsCFBwJhTWBgZcoH9(address)
import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import ImageTk

def gen():
    text = e.get()
    if not text:
        messagebox.showwarning("Error", "Enter text!")
        return

    img = qrcode.make(text).resize((200, 200))
    photo = ImageTk.PhotoImage(img)
    lbl.config(image=photo)
    lbl.image = photo

root = tk.Tk()
root.title("QR Generator")

tk.Label(root, text="Enter Text/URL").pack()
e = tk.Entry(root, width=30)
e.pack()

tk.Button(root, text="Generate", command=gen).pack(pady=5)

lbl = tk.Label(root)
lbl.pack()

root.mainloop()
'''

