from ast import Lambda
from tkinter import *
# from backEnd.database import *

root = Tk() #has to be the first thing that happens first
root.title("Simple Calculator") #main title at the top

e = Entry(root, width = 35, borderwidth=5)
e.grid(row = 0, column = 0 , columnspan=3, padx = 10, pady = 10) #column span refers to how many space of the grid it occupies

def button_add(number):
    # e.delete(0, END) #delete what is already inside the box
    current = e.get() #workaround so that it appends to the number
    e.delete(0, END)
    e.insert(0, str(current) + str(number)) #insert into the box after clicking in the input


def button_erase():
    e.delete(0, END)

#define the buttons

button_1 = Button(root, text = "1", padx = 40, pady = 20, command= lambda: button_add(1))
button_2 = Button(root, text = "2", padx = 40, pady = 20, command= lambda: button_add(2))
button_3 = Button(root, text = "3", padx = 40, pady = 20, command= lambda: button_add(3))
button_4 = Button(root, text = "4", padx = 40, pady = 20, command= lambda: button_add(4))
button_5 = Button(root, text = "5", padx = 40, pady = 20, command= lambda: button_add(5))
button_6 = Button(root, text = "6", padx = 40, pady = 20, command= lambda: button_add(6))
button_7 = Button(root, text = "7", padx = 40, pady = 20, command= lambda: button_add(7))
button_8 = Button(root, text = "8", padx = 40, pady = 20, command= lambda: button_add(8))
button_9 = Button(root, text = "9", padx = 40, pady = 20, command= lambda: button_add(9))
button_0 = Button(root, text = "0", padx = 40, pady = 20, command= lambda: button_add(0))
button_plus = Button(root, text = "+", padx = 39, pady = 20, command = lambda: button_add())
button_equal = Button(root, text="=", padx = 91, pady = 20, command = lambda: button_add())
button_clear = Button(root, text="Clear", padx = 79, pady = 20, command = lambda: button_erase())

#put buttons on the screenbutton_clear.grid()

button_4.grid(row =2 , column =0 )
button_5.grid(row =2 , column =1 )
button_6.grid(row =2 , column =2)

button_7.grid(row =1 , column =0 )
button_8.grid(row =1 , column = 1)
button_9.grid(row =1 , column =2 )

button_0.grid(row =4 , column =0 )

button_plus.grid(row = 5, column=0)
button_equal.grid(row = 5, column= 1, columnspan=2)
button_clear.grid(row = 4, column = 1, columnspan= 2)


#button has the same styles as in css, command is not enclosed with parenthesis after calling function

#create a event loop to figure out what is going on, common for most UI libraries/framework
root.mainloop()