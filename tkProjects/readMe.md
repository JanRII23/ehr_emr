# Lesson 1 --> Basic form
from tkinter import *
## from backEnd.database import *

root = Tk() #has to be the first thing that happens first

#creating a label widget
myLabel = Label(root, text = "Hello World!")


#shoving it onto the screen and displays it
myLabel.pack()


#create a event loop to figure out what is going on (e.g. where the cursor currently is), common for most UI libraries/framework
root.mainloop()

# Lesson 2 --> grid positioning
from tkinter import *
## from backEnd.database import *

root = Tk() #has to be the first thing that happens first

#creating a label widget --> format in one or two steps
myLabel1 = Label(root, text = "Hello World!").grid(row = 0, column=0)
myLabel2 = Label(root, text = "My Name is John Mane!").grid(row = 1, column = 2)


#grid system are relative to each other tkinter just ignores empty values between grid 
#myLabel1.grid(row = 0, column= 0)
#myLabel2.grid(row = 1, column = 0)


#create a event loop to figure out what is going on, common for most UI libraries/framework
root.mainloop()

# Lesson 3 - Buttons
from tkinter import *
## from backEnd.database import *

root = Tk() #has to be the first thing that happens first

def myClick():
    myLabel = Label(root, text = "Look! I clicked")
    myLabel.pack()

#button syntax, state of button can be changed
myButton = Button(root, text = "Click Me!", padx = 50, pady = 50, command = myClick)
myButton.pack()
#button has the same styles as in css, command is not enclosed with parenthesis after calling function

#create a event loop to figure out what is going on, common for most UI libraries/framework
root.mainloop()

# Lesson 4 Input Fields
from tkinter import *
## from backEnd.database import *

root = Tk() #has to be the first thing that happens first

e = Entry(root, width = 50)
e.pack()
e.insert(0, "Enter your Name: ") # refers to prompt what the suggestion input should be

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text = hello)
    myLabel.pack()

#button syntax, state of button can be changed
myButton = Button(root, text = "Enter your name!", padx = 50, pady = 50, command = myClick)
myButton.pack()
#button has the same styles as in css, command is not enclosed with parenthesis after calling function

#create a event loop to figure out what is going on, common for most UI libraries/framework
root.mainloop()


