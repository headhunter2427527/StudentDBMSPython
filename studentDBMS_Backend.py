#backend
import sqlite3

def studentData():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, StdID TEXT, Firstname TEXT, Surname TEXT, DoB TEXT, Age TEXT, Gender TEXT, Address TEXT, Mobile TEXT)")
    con.commit()
    con.close()

def addStdRec(StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("INSERT INTO student VALUES (Null, ?, ?, ?, ?, ?, ?, ?, ?)", StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile)
    con.commit()
    con.close()

def viewData():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    row = cur.fetchall()
    con.close()
    return row

def deleteRec():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id = ?", (id, ))
    con.commit()
    con.close()

def searchData(StdID="", Firstname="", Surname="", DoB="", Age="", Gender="", Address="", Mobile=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student WHERE StdID=? OR Firstname=? OR Surname=? OR DoB=? OR Age=? OR Gender=? OR Address=? OR Mobile=?",(StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile))
    row = cur.fetchall()
    con.close()
    return row

def updateData(id, StdID="", Firstname="", Surname="", DoB="", Age="", Gender="", Address="", Mobile=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("UPDATE student SET StdID=?, Firstname=?, Surname=?, DoB=?, Age=?, Gender=?, Address=?, Mobile=? WHERE id=?", (StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile, id))
    con.commit()
    con.close()


studentData()