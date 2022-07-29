from tkinter import *

root = Tk()
root.title("checkboxes tutorial")
root.geometry("400x400")

var = IntVar()

def show():
    
    myLabel = Label(root, text = var.get()).pack()

c = Checkbutton(root, text = "Check this box", variable = var)
c.pack()


myButton = Button(root, text = "Show Selection" , command = show).pack()

root.mainloop()