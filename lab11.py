import tkinter as tk

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def convert_fahrenheit():
    fahrenheit = float(fahrenheit_entry.get())
    celsius = fahrenheit_to_celsius(fahrenheit)
    celsius_entry.delete(0, tk.END)
    celsius_entry.insert(0, celsius)

def convert_celsius():
    celsius = float(celsius_entry.get())
    fahrenheit = celsius_to_fahrenheit(celsius)
    fahrenheit_entry.delete(0, tk.END)
    fahrenheit_entry.insert(0, fahrenheit)

# Create the main window
window = tk.Tk()
window.title("Temperature Converter")

# Create labels and entry fields
fahrenheit_label = tk.Label(window, text="Fahrenheit:")
fahrenheit_label.grid(row=0, column=0)
fahrenheit_entry = tk.Entry(window)
fahrenheit_entry.grid(row=1, column=0)
fahrenheit_entry.insert(0, 32.0)

celsius_label = tk.Label(window, text="Celsius:")
celsius_label.grid(row=0, column=1)
celsius_entry = tk.Entry(window)
celsius_entry.grid(row=1, column=1)
celsius_entry.insert(0, 0.0)

# Create buttons
fahrenheit_button = tk.Button(window, text=">>>", command=convert_fahrenheit)
fahrenheit_button.grid(row=2, column=0)
celsius_button = tk.Button(window, text="<<<", command=convert_celsius)
celsius_button.grid(row=2, column=1)

# Start the GUI
window.mainloop()

#no 2 
import tkinter as tk

class Account:
    def __init__(self, account_number, holder, balance):
        self.account_number = account_number
        self.holder = holder
        self.balance = balance

def create_account():
    account_number = account_number_entry.get()
    holder = holder_entry.get()
    balance = float(balance_entry.get())
    new_account = Account(account_number, holder, balance)
    # Implement logic to save the account object (e.g., to a database)
    print(f"Account created: {new_account.account_number}, {new_account.holder}, {new_account.balance}")

# Create the main window
window = tk.Tk()
window.title("Create Account")

# Create labels and entry fields
account_number_label = tk.Label(window, text="Account Number:")
account_number_label.grid(row=0, column=0)
account_number_entry = tk.Entry(window)
account_number_entry.grid(row=1, column=0)

holder_label = tk.Label(window, text="Holder:")
holder_label.grid(row=2, column=0)
holder_entry = tk.Entry(window)
holder_entry.grid(row=3, column=0)

balance_label = tk.Label(window, text="Balance:")
balance_label.grid(row=4, column=0)
balance_entry = tk.Entry(window)
balance_entry.grid(row=5, column=0)

# Create the "Create Account" button
create_account_button = tk.Button(window, text="Create Account", command=create_account)
create_account_button.grid(row=6, column=0)

# Start the GUI
window.mainloop()

#no 3
import tkinter as tk

def draw_car(canvas):
    # Car body
    canvas.create_rectangle(50, 50, 200, 150, fill="blue")

    # Tires
    canvas.create_oval(60, 150, 100, 200, fill="black")
    canvas.create_oval(160, 150, 200, 200, fill="black")

def draw_smiling_face(canvas):
    # Face
    canvas.create_oval(100, 50, 300, 300, fill="yellow")

    # Eyes
    canvas.create_oval(150, 100, 200, 200, fill="black")
    canvas.create_oval(250, 100, 300, 200, fill="black")

    # Mouth
    canvas.create_arc(150, 250, 300, 350, start=0, extent=180, fill="black")

# Create the main window
window = tk.Tk()
window.title("Drawing Shapes")

# Create a canvas
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Draw the car
draw_car(canvas)

# Draw the smiling face (optional)
# draw_smiling_face(canvas)

# Start the GUI
window.mainloop()