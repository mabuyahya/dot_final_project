from tkinter import *

def login():
    username = username_entry.get()
    password = password_entry.get()
    password_confirm = confirm_password_entry.get()
    if password == password_confirm and len(password) >= 8:
        label.config(text="Login Successful!", fg="green")
    else:
        label.config(text="Login Failed! Check your password.", fg="red")

window = Tk()
window.title("login form")
window.geometry("500x550")

window.config(bg="lightblue")

label = Label(window, text="Welcome to the Login Form", font=("Arial", 16), bg="lightblue")
label.pack(pady=20)

login_frame = Frame(window, bg="white", width=400, height=450)
login_frame.pack_propagate(False)
login_frame.pack(padx=20, pady=20)

username_label = Label(login_frame, text="Username:", font=("Arial", 14), bg="white")
username_label.pack(pady=5)

username_entry = Entry(login_frame, font=("Arial", 14), bg="white")
username_entry.pack(pady=5)

email_label = Label(login_frame, text="Email:", font=("Arial", 14), bg="white")
email_label.pack(pady=5)

email_entry = Entry(login_frame, font=("Arial", 14), bg="white")
email_entry.pack(pady=5)

number_label = Label(login_frame, text="Phone Number:", font=("Arial", 14), bg="white")
number_label.pack(pady=5)

number_entry = Entry(login_frame, font=("Arial", 14), bg="white")
number_entry.pack(pady=5)

password_label = Label(login_frame, text="Password:", font=("Arial", 14), bg="white")
password_label.pack(pady=5)

password_warning_label = Label(login_frame, text="Password must be at least 8 characters long", font=("Arial", 9), fg="red")
password_warning_label.pack()

password_entry = Entry(login_frame, font=("Arial", 14), bg="white")
password_entry.pack(pady=5)

confirm_password_label = Label(login_frame, text="Confirm Password:", font=("Arial", 14), bg="white")
confirm_password_label.pack(pady=5)

confirm_password_entry = Entry(login_frame, font=("Arial", 14), bg="white")
confirm_password_entry.pack(pady=5)

login_button = Button(login_frame, text="Login", font=("Arial", 14), bg="lightgreen", command=login)
login_button.pack(pady=10)

window.mainloop()