import tkinter as tk
from tkinter import messagebox

def generate_madlib():
    adj = adjective_entry.get()
    verb1 = verb1_entry.get()
    verb2 = verb2_entry.get()
    famous_person = famous_person_entry.get()

    madlib = f"Computer programing is so {adj}! It makes me so excited all the time because \
I love {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

    messagebox.showinfo("Madlib Result", madlib)

# create tkinter window
root = tk.Tk()
root.title("Madlib Generator")

# tags
tk.Label(root, text="Adjective:").grid(row=0, column=0)
tk.Label(root, text="Verb 1:").grid(row=1, column=0)
tk.Label(root, text="Verb 2:").grid(row=2, column=0)
tk.Label(root, text="Famous Person:").grid(row=3, column=0)

# entries
adjective_entry = tk.Entry(root)
verb1_entry = tk.Entry(root)
verb2_entry = tk.Entry(root)
famous_person_entry = tk.Entry(root)

adjective_entry.grid(row=0, column=1)
verb1_entry.grid(row=1, column=1)
verb2_entry.grid(row=2, column=1)
famous_person_entry.grid(row=3, column=1)

# buttons
generate_button = tk.Button(root, text="Generate Madlib", command=generate_madlib)
generate_button.grid(row=4, column=0, columnspan=2)

root.mainloop()
