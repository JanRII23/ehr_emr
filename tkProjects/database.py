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
#             ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#             first_name text,
#             last_name text,
#             address text,
#             city text,
#             state text,
#             zipcode integer
# )""") 
#create a submit button & function

def query():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    #to query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()

    print_records = ''
    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column = 0, columnspan=2)

    conn.commit()
    conn.close()

def submit():
    #store information
    #Whenever you have a function you have to make a curson and a connection
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    #insert into table
    c.execute("INSERT INTO addresses VALUES (NULL, :f_name, :l_name, :address, :city, :state, :zipcode)",

                { #follow the naming convention
                    'f_name': f_name.get(),
                    'l_name': l_name.get(),
                    'address': address.get(),
                    'city': city.get(),
                    'state': state.get(),
                    'zipcode': zipcode.get()
                })

    #make sure when creating a table you set and ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL and when passing it into execute just list as NULL and it will automatically take care of itself --> later one make sure that the primary key is not being show


    #check out how im commiting before deleting info input in the textboxes
    conn.commit()
    conn.close()

    #clear textboxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    state.delete(0, END)
    city.delete(0, END)
    zipcode.delete(0, END)




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

#make a submit button
submit_btn = Button(root, text = "Add Record", command = submit)
submit_btn.grid(row = 6, column = 0, columnspan=2, pady = 10, padx= 10, ipadx= 100)

#create a query button
query_btn = Button(root, text="Show Records", command = query)
query_btn.grid(row=7, column = 0, columnspan=2, pady=10, padx=10, ipadx=137)

#commit changes
conn.commit()

conn.close() #close the connection 

root.mainloop()