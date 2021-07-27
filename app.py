import tkinter as tk # helps create gui
from tkinter import filedialog, Text
import os # allows us to run the app

root = tk.Tk() # html - body; holds the entire structure
apps =  [] # contains the location of the files we open

# load up text file to see what we've saved
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()] # don't add if it's just a blank space

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

def runApps():
    for app in apps:
        os.startfile(app) # start all of the apps in the list

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
runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

# whenever we close our app, write all saved apps to save file
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')