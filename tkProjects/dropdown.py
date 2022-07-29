from tkinter import *

root = Tk()

root.title('drop down menu')

root.geometry("400x400")

def show():
    myLabel = Label(root, text = clicked.get()).pack()


options = [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"
]


clicked = StringVar()
clicked.set(options[0]) #making sure there is a default variable to show instead of a just a blank


drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text = "Show SElection", command = show).pack()

root.mainloop()
