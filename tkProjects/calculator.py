from ast import Lambda
import math
from tkinter import *
# from backEnd.database import *

root = Tk() #has to be the first thing that happens first
root.title("Simple Calculator") #main title at the top

e = Entry(root, width = 35, borderwidth=5)
e.grid(row = 0, column = 0 , columnspan=3, padx = 10, pady = 10) #column span refers to how many space of the grid it occupies

def button_click(number):
    # e.delete(0, END) #delete what is already inside the box
    current = e.get() #workaround so that it appends to the number
    e.delete(0, END)
    e.insert(0, str(current) + str(number)) #insert into the box after clicking in the input


def button_erase():
    e.delete(0, END)

def button_add():
    firstNum = e.get() #numbers can be passed as function arguments
    global f_num #use the global keyword to set a variable as global
    global math
    math = "add"
    f_num = int(firstNum)
    e.delete(0, END) #deletes the textbox
    

def button_equals():
    secondNum = e.get()
    e.delete(0, END)
    if (math == "add"):
        e.insert(0, f_num + int(secondNum))
    elif (math == "sub"):
        e.insert(0, f_num - int(secondNum))
    elif (math == "div"):
        e.insert(0, f_num / int(secondNum))
    elif (math == "mult"):
        e.insert(0, f_num * int(secondNum))
    
    #recognize the logic implemented above it actually makes sense
    #notice that despite having the keyword global its not accessible if the function is not called/ instantiated

def subtract():
    firstNum = e.get() 
    global f_num
    global math
    math = "sub"
    f_num = int(firstNum)
    e.delete(0, END)

def divide():
    firstNum = e.get() 
    global f_num
    global math
    math = "div"
    f_num = int(firstNum)
    e.delete(0, END)

def multiply():
    firstNum = e.get() 
    global f_num
    global math
    math = "mult"
    f_num = int(firstNum)
    e.delete(0, END)

#define the buttons

button_1 = Button(root, text = "1", padx = 40, pady = 20, command= lambda: button_click(1))
button_2 = Button(root, text = "2", padx = 40, pady = 20, command= lambda: button_click(2))
button_3 = Button(root, text = "3", padx = 40, pady = 20, command= lambda: button_click(3))
button_4 = Button(root, text = "4", padx = 40, pady = 20, command= lambda: button_click(4))
button_5 = Button(root, text = "5", padx = 40, pady = 20, command= lambda: button_click(5))
button_6 = Button(root, text = "6", padx = 40, pady = 20, command= lambda: button_click(6))
button_7 = Button(root, text = "7", padx = 40, pady = 20, command= lambda: button_click(7))
button_8 = Button(root, text = "8", padx = 40, pady = 20, command= lambda: button_click(8))
button_9 = Button(root, text = "9", padx = 40, pady = 20, command= lambda: button_click(9))
button_0 = Button(root, text = "0", padx = 40, pady = 20, command= lambda: button_click(0))
button_plus = Button(root, text = "+", padx = 39, pady = 20, command = button_add) #lambda argument only needed if an argument is being passed check syntax
button_equal = Button(root, text="=", padx = 91, pady = 20, command = button_equals)
button_clear = Button(root, text="Clear", padx = 79, pady = 20, command = button_erase)

button_subtract = Button(root, text = "-", padx = 42, pady = 20, command = subtract)
button_divide = Button(root, text = "/", padx = 42, pady = 20, command = divide)
button_multiply = Button(root, text = "*", padx = 42, pady = 20, command = multiply)

#put buttons on the screenbutton_clear.grid()

button_4.grid(row =2 , column =0 )
button_5.grid(row =2 , column =1 )
button_6.grid(row =2 , column =2)

button_7.grid(row =1 , column =0 )
button_8.grid(row =1 , column = 1)
button_9.grid(row =1 , column =2 )

button_1.grid(row= 3, column = 0)
button_2.grid(row= 3, column = 1)
button_3.grid(row= 3, column = 2)

button_0.grid(row =4 , column =0 )

button_plus.grid(row = 5, column=0)
button_equal.grid(row = 5, column= 1, columnspan=2)
button_clear.grid(row = 4, column = 1, columnspan= 2)

button_subtract.grid(row = 6, column=0)
button_divide.grid(row = 6, column = 1)
button_multiply.grid(row = 6, column = 2)


#button has the same styles as in css, command is not enclosed with parenthesis after calling function

#create a event loop to figure out what is going on, common for most UI libraries/framework
root.mainloop()