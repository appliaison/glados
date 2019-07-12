from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Button, Style, Label
from random import choice

exps = ["Welcome to Glados", 
"Where do you want to go today?"]

root = Tk()
root.title("Welcome to GladOS")

lb = Label(root, text="HELLO")
lb.pack(pady=30)

def express():
    lb["text"] = choice(exps)
    
Button(root, text="Activate Glados", command=express).pack(pady=20)
root.geometry("250x150+300+300")

root.mainloop()
