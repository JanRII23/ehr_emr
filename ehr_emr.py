#Frontend

from tkinter import*
import tkinter.messagebox


#import database

#refine the interface later and find some ecamples of industry ready ehr/emr

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

            ButtonFrame = Frame(MainFrame, bd=2, width = 1350, height = 70, padx=18, pady=10, bg = "Ghost White", relief = RIDGE)
            ButtonFrame.pack(side=BOTTOM)

            DataFrame = Frame(MainFrame, bd=1, width = 1300, height = 400, padx= 20, pady= 20, bg = "cadet blue", relief = RIDGE)
            DataFrame.pack(side=BOTTOM)

            DataFrameLEFT = LabelFrame(DataFrame, bd=1, width = 1000, height = 600, padx = 20, relief = RIDGE, bg ="Ghost White", font=('arial', 20, 'bold'), text = "Student Info\n")
            DataFrameLEFT.pack(side=LEFT)

            DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width = 450, height = 300, padx=31, pady=3, bg = "Ghost White", relief = RIDGE, font=('arial', 20, 'bold'), text = "Student Details\n")
            DataFrameRIGHT.pack(side=RIGHT)

            
            #========================================LABELS & ENTRY Widgets=======================
            self.lblStdID = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Student ID:", padx = 2, pady = 2, bg="Ghost White")
            self.lblStdID.grid(row = 0, column = 0, sticky = W)
            self.txtStdID = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=StdID, width = 39)
            self.txtStdID.grid(row = 0, column = 1)

            self.lblfna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Firstname:", padx = 2, pady = 2, bg="Ghost White")
            self.lblfna.grid(row = 1, column = 0, sticky = W)
            self.txtfna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=FirstName, width = 39)
            self.txtfna.grid(row = 1, column = 1)

            self.lblSna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Surname:", padx = 2, pady = 2, bg="Ghost White")
            self.lblSna.grid(row = 2, column = 0, sticky = W)
            self.txtSna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Surname, width = 39)
            self.txtSna.grid(row = 2, column = 1)

            self.lblDoB = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Date of Birth:", padx = 2, pady = 3, bg="Ghost White")
            self.lblDoB.grid(row = 3, column = 0, sticky = W)
            self.txtDoB = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=DoB, width = 39)
            self.txtDoB.grid(row = 3, column = 1)

            self.lblAge = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Age:", padx = 2, pady = 3, bg="Ghost White")
            self.lblAge.grid(row = 4, column = 0, sticky = W)
            self.txtAge = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Age, width = 39)
            self.txtAge.grid(row = 4, column = 1)

            self.lblGender = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Gender:", padx = 2, pady = 3, bg="Ghost White")
            self.lblGender.grid(row = 5, column = 0, sticky = W)
            self.txtGender = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Gender, width = 39)
            self.txtGender.grid(row = 5, column = 1)


            self.lblAdr = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Address:", padx = 2, pady = 3, bg="Ghost White")
            self.lblAdr.grid(row = 6, column = 0, sticky = W)
            self.txtAdr = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Address, width = 39)
            self.txtAdr.grid(row = 6, column = 1)

            self.lblMobile = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Mobile:", padx = 2, pady = 3, bg="Ghost White")
            self.lblMobile.grid(row = 7, column = 0, sticky = W)
            self.txtMobile = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Mobile, width = 39)
            self.txtMobile.grid(row = 7, column = 1)

             #========================================ListBox & Scroll Bar Widgets=======================

            scrollbar = Scrollbar(DataFrameRIGHT)
            scrollbar.grid(row=0, column = 1, sticky='ns')

            studentlist = Listbox(DataFrameRIGHT, width = 41, height = 15, font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set, bg = "Black")
            studentlist.grid(row=0, column = 0, padx= 8)
            scrollbar.config(command = studentlist.yview)

            #========================================Button Widgets=======================

            self.btnAddDate = Button(ButtonFrame, text = "Add New", font=('arial', 20, 'bold'), height = 1, width = 10, bd= 4)
            self.btnAddDate.grid(row=0, column = 0)

            self.btnDisplayData = Button(ButtonFrame, text = "Display", font=('arial', 20, 'bold'), height = 1, width = 10, bd= 4)
            self.btnDisplayData.grid(row=0, column = 1)

            self.btnClearData = Button(ButtonFrame, text = "Clear", font=('arial', 20, 'bold'), height = 1, width = 10, bd= 4)
            self.btnClearData.grid(row=0, column = 2)

            self.btnDeleteData = Button(ButtonFrame, text = "Delete", font=('arial', 20, 'bold'), height = 1, width = 10, bd= 4)
            self.btnDeleteData.grid(row=0, column = 3)

            self.btnSearchData = Button(ButtonFrame, text = "Search", font=('arial', 20, 'bold'), height = 1, width = 10, bd= 4)
            self.btnSearchData.grid(row=0, column = 4)

            self.btnUpdateData = Button(ButtonFrame, text = "Update", font=('arial', 20, 'bold'), height = 1, width = 10, bd= 4)
            self.btnUpdateData.grid(row=0, column = 5)

            self.btnExit = Button(ButtonFrame, text = "Exit", font=('arial', 20, 'bold'), height = 1, width = 10, bd= 4)
            self.btnExit.grid(row=0, column = 6)




if __name__=='__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()
