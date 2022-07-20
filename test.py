#Frontend
from tkinter import*
import tkinter.messagebox

#import database

class Student:
        def __init__(self,root):
            self.root = root
            self.root.title("Database Management System")
            self.root.geometry("1350x750+0+0")
            self.root.config(bg="cadet blue")

            StdID = StringVar()
            FirstName = StringVar()
            Surname = StringVar()
            DoB = StringVar()
            Age = StringVar()
            Gender = StringVar()
            Address = StringVar()
            Mobile = StringVar()

            #========================================FRAMES=======================
            MainFrame = Frame(self.root, bg = "cadet blue")
            MainFrame.grid()

            TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg = "Ghost White", relief = RIDGE)
            TitFrame.pack(side=TOP)

            self.lblTit = Label(TitFrame, font=('arial', 47, 'bold'), text="Database Management System", bg="Ghost White")
            self.lblTit.grid()



