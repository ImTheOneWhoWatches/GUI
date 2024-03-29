import tkinter as tk
from tkinter import messagebox, PhotoImage, Menu
import os

def close_program(event=None):
    save_notes()
    if messagebox.askokcancel("Quit", "Do you want to quit the program?"):
        root.destroy()

def show_context_menu(event):
    context_menu = Menu(root, tearoff=0)
    context_menu.add_command(label="Exit", command=close_program)
    context_menu.post(event.x_root, event.y_root)

def save_notes():
    try:
        with open("assets/notes.txt", "w") as file:
            text_content = text.get("1.0", "end-1c")
            file.write(text_content)
        print("Notes saved successfully")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save notes: {e}")
        print(f"Failed to save notes: {e}")

def open_notes():
    try:
        with open("assets/notes.txt", "r") as file:
            notes = file.read()
            text.insert(tk.END, notes)
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No previous notes found.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open notes: {e}")

def auto_save():
    save_notes()
    root.after(5000, auto_save)  # 5 seconds in milliseconds

root = tk.Tk()
root.title("Notebook")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = int(screen_width * 0.9)
window_height = int(screen_height * 0.9)
root.geometry(f"{window_width}x{window_height}+{int((screen_width - window_width) / 2)}+{int((screen_height - window_height) / 2)}")

image_path = r"C:\Users\Inbou\Desktop\TEST\Assets\BackgroundImage.png"
if not os.path.exists(image_path):
    print("Image file not found:", image_path)
    exit()

background_image = PhotoImage(file=image_path)
bg_image = tk.Label(root, image=background_image)
bg_image.place(relheight=1, relwidth=1)

text = tk.Text(root, wrap="word", bg="white")
text.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

open_notes()
auto_save()

root.bind('<Escape>', close_program)
root.bind('<Button-3>', show_context_menu)

root.mainloop()
