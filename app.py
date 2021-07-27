import tkinter as tk # helps create gui
from tkinter import filedialog, Text
import os # allows us to run the app

root = tk.Tk() # html - body; holds the entire structure
apps =  [] # contains the location of the files we open

# open files, click on the file, and save
# only allows executables
def addApp():

    for widget in frame.winfo_children():
        widget.destroy() # when updating, delete previous widgets

    filename = filedialog.askopenfilename(initialdir="/", title="select File",
    filetypes=(("executables", "*.exe"), ("all files", "*.*")))

    apps.append(filename) # add to our list of apps
    print(filename)

    for app in apps:
        label = tk.Label(frame, text=app, bg="gray") # label of the app
        label.pack()

# making the canvas bigger
canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
# attach to root
canvas.pack()

# add another element
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# add buttons
openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()

# run apps button
runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42")
runApps.pack()

root.mainloop()