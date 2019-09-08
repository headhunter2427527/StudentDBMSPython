#Frontend

from tkinter import *
import tkinter.messagebox
import studentDBMS_Backend

class Student:

    def __init__(self, root):
        self.root = root
        self.root.title("Student Database Management System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="grey")

        StdID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        DoB = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()

        # ==========================================Functions============================================

        def iExit():
            iExit = tkinter.messagebox.askyesno("Student Database Management System", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def clearData():
            self.textStudentID.delete(0, END)
            self.textFirstName.delete(0, END)
            self.textSurName.delete(0, END)
            self.textDoB.delete(0, END)
            self.textAge.delete(0, END)
            self.textGender.delete(0, END)
            self.textAddress.delete(0, END)
            self.textMobile.delete(0, END)

        def addData():
            if(len(StdID.get())!=0):
                studentDBMS_Backend.addStdRec(StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get())
                studentList.delete(0, END)
                studentList.insert(END, (StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get()))

        def displayData():
            studentList.delete(0, END)
            for row in studentDBMS_Backend.viewData():
                studentList.insert(END, row, str(""))

        def studentRec(event):
            global sd
            searchStudent = studentList.curselection()[0]
            sd = studentList.get(searchStudent)

            self.textStudentID.delete(0, END)
            self.textStudentID.insert(END, sd[1])
            self.textFirstName.delete(0, END)
            self.textFirstName.insert(END, sd[2])
            self.textSurName.delete(0, END)
            self.textSurName.insert(END, sd[3])
            self.textDoB.delete(0, END)
            self.textDoB.insert(END, sd[4])
            self.textAge.delete(0, END)
            self.textAge.insert(END, sd[5])
            self.textGender.delete(0, END)
            self.textGender.insert(END, sd[6])
            self.textAddress.delete(0, END)
            self.textAddress.insert(END, sd[7])
            self.textMobile.delete(0, END)
            self.textMobile.insert(END, sd[8])


        def deleteData():
            if (len(StdID.get()) != 0):
                studentDBMS_Backend.deleteRec(sd[0])
                clearData()
                displayData()

        def searchData():
            studentList.delete(0, END)
            for row in studentDBMS_Backend.searchData(StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get()):
                studentList.insert(END, row, str(""))

        def updateData():
            if(len(StdID.get)!=0):
                studentDBMS_Backend.deleteRec(sd[0])
            if(len(StdID.get!=0)):
                studentDBMS_Backend.addStdRec(StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get())
                studentList.delete(0, END)
                studentList.insert(END, (StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get()))

        #==========================================Frame============================================
        MainFrame = Frame(self.root, bg="grey")
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd = 2, padx = 54, pady = 8, bg = "Ghost White", relief = RIDGE)
        TitleFrame.pack(side = TOP)

        self.labelTitle = Label(TitleFrame, font = ('arial', 47, 'bold'), text = "Student Database Management System", bg = "Ghost White")
        self.labelTitle.grid()

        ButtonFrame = Frame(MainFrame, bd = 2, width = 1350, height = 70, padx = 18, pady = 10, bg = "Ghost White", relief = RIDGE)
        ButtonFrame.pack(side = BOTTOM)

        DataFrame = Frame(MainFrame, bd = 1, width = 1300, height = 400, padx = 20, pady = 20, relief = RIDGE, bg = "grey")
        DataFrame.pack(side = BOTTOM)

        DataFrameLeft = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, relief=RIDGE, bg="Ghost White", font = ('arial', 20, 'bold'), text = "Student Information\n")
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE, bg="Ghost White", font = ('arial', 20, 'bold'), text = "Student Details\n")
        DataFrameRight.pack(side=RIGHT)

        #==========================================Labels and Entry Widget======================================================

        self.labelStudentID = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Student ID : ", padx = 2, pady = 2,bg = "Ghost White")
        self.labelStudentID.grid(row = 0, column = 0, sticky = W)
        self.textStudentID = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable = StdID, width = 39)
        self.textStudentID.grid(row=0, column=1)

        self.labelFirstName = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="First Name : ", padx=2, pady=2, bg="Ghost White")
        self.labelFirstName.grid(row=1, column=0, sticky=W)
        self.textFirstName = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=Firstname, width=39)
        self.textFirstName.grid(row=1, column=1)

        self.labelSurName = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Surname : ", padx=2, pady=2, bg="Ghost White")
        self.labelSurName.grid(row=2, column=0, sticky=W)
        self.textSurName = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=Surname, width=39)
        self.textSurName.grid(row=2, column=1)

        self.labelDoB = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="DoB : ", padx=2, pady=2, bg="Ghost White")
        self.labelDoB.grid(row=3, column=0, sticky=W)
        self.textDoB = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=DoB, width=39)
        self.textDoB.grid(row=3, column=1)

        self.labelAge = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Age : ", padx=2, pady=2, bg="Ghost White")
        self.labelAge.grid(row=4, column=0, sticky=W)
        self.textAge = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=Age, width=39)
        self.textAge.grid(row=4, column=1)

        self.labelGender = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Gender : ", padx=2, pady=2, bg="Ghost White")
        self.labelGender.grid(row=5, column=0, sticky=W)
        self.textGender = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=Gender, width=39)
        self.textGender.grid(row=5, column=1)

        self.labelAddress = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Address : ", padx=2, pady=2, bg="Ghost White")
        self.labelAddress.grid(row=6, column=0, sticky=W)
        self.textAddress = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=Address, width=39)
        self.textAddress.grid(row=6, column=1)

        self.labelMobile = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Mobile : ", padx=2, pady=2, bg="Ghost White")
        self.labelMobile.grid(row=7, column=0, sticky=W)
        self.textMobile = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=Mobile, width=39)
        self.textMobile.grid(row=7, column=1)

        # ==========================================ListBox & ScrollBar Widget======================================================

        scrollBar = Scrollbar(DataFrameRight)
        scrollBar.grid(row = 0, column = 1, sticky = 'ns')

        studentList = Listbox(DataFrameRight, width = 41, height = 16, font=('arial', 12, 'bold'), yscrollcommand = scrollBar.set)
        studentList.bind('<<ListboxSelect>>', studentRec)
        studentList.grid(row = 0, column = 0, padx = 8)
        scrollBar.config(command = studentList.yview)

        # ==========================================Button Widget======================================================

        self.buttonAddData = Button(ButtonFrame, text = "Add New", font = ('arial', 20, 'bold'), height = 1, width = 10, bd = 4, command = addData)
        self.buttonAddData.grid(row = 0, column = 0)

        self.buttonDisplayData = Button(ButtonFrame, text="Display", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command = displayData)
        self.buttonDisplayData.grid(row=0, column=1)

        self.buttonClearData = Button(ButtonFrame, text="Clear", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command = clearData)
        self.buttonClearData.grid(row=0, column=2)

        self.buttonDeleteData = Button(ButtonFrame, text="Delete", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command = deleteData)
        self.buttonDeleteData.grid(row=0, column=3)

        self.buttonSearchData = Button(ButtonFrame, text="Search", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command = searchData)
        self.buttonSearchData.grid(row=0, column=4)

        self.buttonUpdateData = Button(ButtonFrame, text="Update", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command = updateData)
        self.buttonUpdateData.grid(row=0, column=5)

        self.buttonExit = Button(ButtonFrame, text="Exit", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command = iExit)
        self.buttonExit.grid(row=0, column=6)




if __name__=='__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()