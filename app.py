import tkinter as tk # helps create gui
from tkinter import filedialog, Text
import os # allows us to run the app

root = tk.Tk() # html - body; holds the entire structure

# making the canvas bigger
canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
# attach to root
canvas.pack()

# add another element
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# add buttons
openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42")
openFile.pack()

root.mainloop()