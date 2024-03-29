import tkinter as tk
from tkinter import messagebox, PhotoImage, Menu
import os

def close_program(event=None):
    if messagebox.askokcancel("Quit", "Do you want to quit the program?"):
        root.destroy()

def show_context_menu(event):
    context_menu = Menu(root, tearoff=0)
    context_menu.add_command(label="Exit", command=close_program)
    context_menu.post(event.x_root, event.y_root)

def open_calculator():
    os.system("start cmd /k python assets\\Calculator.py")

def open_notebook():
    os.system("start cmd /k python assets\\Notebook.py")

root = tk.Tk()
root.title("TheOneClient")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the size of the window (90% of screen width and height)
window_width = int(screen_width * 0.9)
window_height = int(screen_height * 0.9)

# Set the window size and position it in the center of the screen
root.geometry(f"{window_width}x{window_height}+{int((screen_width - window_width) / 2)}+{int((screen_height - window_height) / 2)}")

# Load the image
image_path = r"C:\Users\Inbou\Desktop\TEST\Assets\BackgroundImage.png"
if not os.path.exists(image_path):
    print("Image file not found:", image_path)
    exit()

background_image = PhotoImage(file=image_path)

# Create a Label widget to display the background image
bg_image = tk.Label(root, image=background_image)
bg_image.place(relheight=1, relwidth=1)  # Fill the entire window

# Create a button named "Calculator" with the calculator icon on the top-left corner
calculator_icon_path = r"C:\Users\Inbou\Desktop\TEST\Assets\CalculatorImg.png"
if not os.path.exists(calculator_icon_path):
    print("Calculator icon file not found:", calculator_icon_path)
    exit()

calculator_icon = PhotoImage(file=calculator_icon_path)
calculator_button = tk.Button(root, text="Calculator", command=open_calculator, image=calculator_icon, compound="top")
calculator_button.place(x=10, y=10)  # Place the button in the top-left corner

# Create a button named "Notebook" with the notebook icon on the top-right corner
notebook_icon_path = r"C:\Users\Inbou\Desktop\TEST\Assets\Notebook.png"
if not os.path.exists(notebook_icon_path):
    print("Notebook icon file not found:", notebook_icon_path)
    exit()

notebook_icon = PhotoImage(file=notebook_icon_path)
notebook_button = tk.Button(root, text="Notebook", command=open_notebook, image=notebook_icon, compound="top")
notebook_button.place(relx=1.0, rely=0, anchor='ne', x=-10, y=10)  # Place the button in the top-right corner

# Bind the 'Escape' key to the close_program function
root.bind('<Escape>', close_program)

# Bind right-click event to show the context menu
root.bind('<Button-3>', show_context_menu)

root.mainloop() 