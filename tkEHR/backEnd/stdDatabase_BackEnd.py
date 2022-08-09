import sqlite3
#backend

#figure out how to globalize con, cur inside of repeating each time in the function
#there is an insert missing info to a table using cur.execute INSERT INTO tableName VALUES (pass in a value if a filled) make sure to try doing it with ? if missing in display table


#create a table, nameVar DATATYPE (five types NULL, INTEGER, REAL, TEXT, BLOB)
def studentData():

    #connect to the database
    con = sqlite3.connect("student.db")

    #create a cursor
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS student (
                   id INTEGER PRIMARY KEY,
                   StdID text,
                   Firstname text,
                   Surname text,
                   DoB text,
                   Age text,
                   Gender text,
                   Address text,
                   Mobile text   
    
    )""")
    #commit the command
    con.commit()
    #close the connection
    con.close()


# def studentData():
#     con = sqlite3.connect("student.db")
#     cur = con.cursor()
#     cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, StdID text, Firstname text, Surname text, DoB text, Age text, Gender text, Address text, Mobile text)")
#     con.commit()
#     con.close()

def addStdRec(StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile): # why is he passing an extra value in and what is the null for?
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("INSERT INTO student VALUES(NULL, ?,?,?,?,?,?,?,?)", (StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile))
    con.commit()
    con.close()

def viewData():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    con.close()
    return rows

def deleteRec(id):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id = ?", (id,))
    con.commit()
    con.close()

def searchData(StdID="",Firstname="", Surname="", DoB="", Age="", Gender="", Address="", Mobile=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student WHERE StdID=? OR Firstname=? OR Surname=? OR DoB=? OR Age=? OR Gender=? OR Address=? OR Mobile=?", (StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile))
    rows=cur.fetchall()
    con.close()
    return rows


def dataUpdate(id, StdID="",Firstname="", Surname="", DoB="", Age="", Gender="", Address="", Mobile=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("UPDATE student SET StdID=?, Firstname=?, Surname=?, DoB=?, Age=?, Gender=?, Address=?, Mobile=?, WHERE id=?", (StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile, id))
    con.commit()
    con.close()

studentData()


