from tkinter import *


root = Tk()
root.title('Learning SQLite3')

#make sure to keep in mind how the labels are packed to 

#Toplevel is basically another window that popups and can be attached to buttons

def open():
    
    top = Toplevel()
    top.title('My 2nd Window')

btn = Button(root, text="Open Second Window", command = open).pack()

root.mainloop()

#files can be read in the too in sqlite