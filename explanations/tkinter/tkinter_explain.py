from tkinter import *

window = Tk()
window.title("login page")
window.geometry("500x450")
window.config(bg="lightblue")

label = Label(window, text="welcome to calculator", font=("Arial", 16), bg="lightblue")
label.pack(padx=20, pady=20)
login = Frame(window, bg="white", width=400, height=300)
login.pack_propagate(False)
login.pack(padx=20, pady=20, side="bottom")

first_label = Label(login, text="inter your first number", font=("Arial", 14), bg="white")
first_label.pack(pady=5)

first_entry = Entry(login, font=("Arial", 14), bg="white")
first_entry.pack(pady=5)

second_label = Label(login, text="inter your second number", font=("Arial", 14), bg="white")
second_label.pack(pady=5)

second_entry = Entry(login, font=("Arial", 14), bg="white")
second_entry.pack(pady=5)

operation_label = Label(login, text="inter you operation:", font=("Arial", 14), bg="white")
operation_label.pack(pady=5)

operation_entry = Entry(login, font=("Arial", 14), bg="white")
operation_entry.pack(pady=5)

calculate_button = Button(login, text="Calculate", font=("Arial", 14), bg="lightgreen", command=lambda: math())
calculate_button.pack(pady=10)

result_label = Label(login, text="Result: ", font=("Arial", 14), bg="white", fg="blue")
result_label.pack(pady=5)

def math():
    first_number = float(first_entry.get())
    second_number = float(second_entry.get())
    operation = operation_entry.get()
    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number != 0:
            result = first_number / second_number
        else:
            result = "Error: Division by zero"
    else:
        result = "Invalid operation"
    result_label.config(text=f"Result: {result}")


window.mainloop()