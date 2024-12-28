import tkinter as tk
import math

# Variable to store the value in memory
memory = None

# Functions for basic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Functions for additional operations
def square_root():
    try:
        value = float(entry.get())
        result = math.sqrt(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def power():
    try:
        expression = entry.get()
        base, exponent = map(float, expression.split('^'))
        result = math.pow(base, exponent)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to handle button presses
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)  # Clear current text in the input field
    entry.insert(tk.END, current + value)

# Function to calculate the result
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)

        # Add expression and result to the history
        history_text.insert(tk.END, f"{expression} = {result}\n")
        history_text.yview(tk.END)  # Scroll down

    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the screen
def clear():
    entry.delete(0, tk.END)

# Function to store value in memory
def memory_store():
    global memory
    try:
        memory = float(entry.get())
    except ValueError:
        memory = None

# Function to recall value from memory
def memory_recall():
    if memory is not None:
        entry.delete(0, tk.END)
        entry.insert(tk.END, memory)
    else:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "No data in memory")

# Function to clear memory
def memory_clear():
    global memory
    memory = None

# Create the application window
root = tk.Tk()
root.title("Calculator")

# Set the window size
root.geometry("400x750")
root.config(bg="#F2F2F7")  # Light background, similar to Apple style

# Create the input field
entry = tk.Entry(root, width=20, borderwidth=5, font=("Helvetica Neue", 20), bd=10, relief="sunken", justify="right",
                 fg="#1C1C1E", bg="#FFFFFF")
entry.grid(row=0, column=0, columnspan=4, pady=20)

# List of calculator buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0), ('(', 5, 1), (')', 5, 2),
    ('MS', 5, 3), ('MR', 6, 0), ('MC', 6, 1),
    ('√', 6, 2), ('^', 6, 3)
]

# Button style settings
button_style = {
    "width": 10,
    "height": 3,
    "font": ("Helvetica Neue", 16),
    "bd": 4,
    "fg": "#1C1C1E",  # Dark text
    "bg": "#DDDDDD",  # Light gray background for buttons
    "activebackground": "#D1D1D6"  # Button background color when pressed
}

# Update the style for operation buttons
button_style_alt = {
    "width": 10,
    "height": 3,
    "font": ("Helvetica Neue", 16),
    "bd": 4,
    "fg": "#FFFFFF",  # White text for operations
    "bg": "#FF3B30",  # Red for operations
    "activebackground": "#FF2D1A"  # Darker red when pressed
}

# Create the buttons and place them on the grid
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, **button_style, command=calculate)
    elif text == "C":
        button = tk.Button(root, text=text, **button_style, command=clear)
    elif text == "MS":
        button = tk.Button(root, text=text, **button_style, command=memory_store)
    elif text == "MR":
        button = tk.Button(root, text=text, **button_style, command=memory_recall)
    elif text == "MC":
        button = tk.Button(root, text=text, **button_style, command=memory_clear)
    elif text == "√":
        button = tk.Button(root, text=text, **button_style_alt, command=square_root)
    elif text == "^":
        button = tk.Button(root, text=text, **button_style_alt, command=power)
    else:
        button = tk.Button(root, text=text, **button_style, command=lambda value=text: button_click(value))

    button.grid(row=row, column=col, padx=5, pady=5)

# Create the history display widget
history_label = tk.Label(root, text="History:", font=("Helvetica Neue", 14), bg="#F2F2F7", fg="#1C1C1E")
history_label.grid(row=7, column=0, columnspan=4)

history_text = tk.Text(root, height=10, width=30, font=("Helvetica Neue", 14), bd=5, relief="sunken", fg="#1C1C1E",
                       bg="#F7F7F7")
history_text.grid(row=8, column=0, columnspan=4, padx=5, pady=5)

# Start the main loop of the application
root.mainloop()