
from tkinter import Tk, Label, Button, Entry, StringVar

# Function to update the expression in the entry box
def press(key):
    current = expression.get()
    expression.set(current + str(key))

# Function to evaluate the expression
def evaluate():
    try:
        result = eval(expression.get())  # Evaluates the mathematical expression
        expression.set(result)
    except:
        expression.set("Error")

# Function to clear the expression
def clear():
    expression.set("")

# Setting up the application window
window = Tk()
window.title("Simple Calculator")
window.geometry("600x500")
window.resizable(False, False)
window.configure(bg="gray")  # Background color for the window

# String variable to store the expression
expression = StringVar()

# Creating the entry box for input
entry = Entry(window, textvariable=expression, font=("Arial", 24), bd=10, relief="sunken", justify="right", bg="gray", fg="white")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Creating the calculator buttons with modern layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0, 4)  # Clear button spans across 4 columns
]

# Adding buttons to the window
for (text, row, col, *span) in buttons:
    button = Button(window, text=text, width=10, height=2, font=("Arial", 14), fg="white", bg="gray", activebackground="gray", command=lambda t=text: press(t) if t != "=" and t != "C" else evaluate() if t == "=" else clear())
    button.grid(row=row, column=col, columnspan=span[0] if span else 1, padx=5, pady=5)

# Run the application
window.mainloop()
