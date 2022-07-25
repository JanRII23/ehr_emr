import sqlite3
from venv import create



def createDatabase():

    #connect to the database
    con = sqlite3.connect("customer.db")

    #create a cursor
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS customers (
                   firstName text,
                   lastName text
    
    )""")
    #commit the command
    con.commit()
    #close the connection
    con.close()


#query all function
def show_all():
    #making a connection
    conn = sqlite3.connect('../customer.db')

    # create a cursor
    cur = conn.cursor()
    cur.execute("SELECT * FROM customers")
    items = cur.fetchall()

    for i in items:
        print(items)

    #commit command
    conn.commit()

    #close the commit
    conn.close()
                
def insertValues():
    con = sqlite3.connect('customer.db')
    cur = con.cursor()

    many_val = [
                ('Wes', 'Brown'),
                ('John', 'Cash'),
                ]

    cur.executemany("INSERT INTO customer VALUES(?,?)", many_val)

    con.commit()
    con.close()

show_all()