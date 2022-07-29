from tkinter import *

import sqlite3


root = Tk()

#Databases

#create a database or connect to one
conn = sqlite3.connect('address_book.db')

#create a cursor, sends off the command
c = conn.cursor()

#create table
# c.execute("""CREATE TABLE addresses (
#             first_name text,
#             last_name text,
#             address text,
#             city text,
#             state text,
#             zipcode, integer
# )""") you only create a table one time

#create a submit button & function

def submit():
    #store information
    #Whenever you have a function you have to make a curson and a connection
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    #clear textboxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    state.delete(0, END)
    city.delete(0, END)
    zipcode.delete(0, END)

    conn.commit()
    conn.close()



#create textboxes
f_name = Entry(root, width = 30)
f_name.grid(row=0, column = 1, padx = 20)

l_name = Entry(root, width = 30)
l_name.grid(row=1, column = 1, padx = 20)

address = Entry(root, width = 30)
address.grid(row=2, column = 1, padx = 20)

city = Entry(root, width = 30)
city.grid(row=3, column = 1, padx = 20)

state = Entry(root, width = 30)
state.grid(row=4, column = 1, padx = 20)

zipcode = Entry(root, width = 30)
zipcode.grid(row=5, column = 1, padx = 20)

#create text box labels
f_name_label = Label(root, text = "First Name")
f_name_label.grid(row = 0, column = 0)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row = 1, column = 0)

address_label = Label(root, text="Address")
address_label.grid(row = 2, column = 0)

city_label = Label(root, text = "City")
city_label.grid(row = 3, column = 0)

state_label = Label(root, text = "State")
state_label.grid(row = 4, column = 0)

zipcode_label = Label(root, text = "Zipcode")
zipcode_label.grid(row = 5, column = 0)


submit_btn = Button(root, text = "Add Record", command = submit)
submit_btn.grid(row = 6, column = 0, columnspan=2, pady = 10, padx= 10, ipadx= 100)

#commit changes
conn.commit()

conn.close() #close the connection 

root.mainloop()