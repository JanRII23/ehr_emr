from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Learn to Code")

# types of messagebox, (showinfo, showwarning, showerror, askquestion, askokcancel, askyesorno)

#popups can be used to debug like console.log

def popup():
    messagebox.showinfo("This is my popup!", "Hello") #first string is the title bar, second is the information in the popup screen

Button(root, text = "Popup", command = popup).pack()


root.mainloop()