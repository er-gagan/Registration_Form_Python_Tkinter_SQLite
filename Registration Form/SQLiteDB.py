import sqlite3
from sqlite3.dbapi2 import Cursor

connection = sqlite3.connect('student_database.sql')
c = connection.cursor()

def SendDB(Fname,Mname,Lname,Phone1,Phone2,Pin,Current_address,Permanent_address,City,State,Gender,Area_Of_Intrest,Age,Email,Suggession):
    
    c.execute('CREATE TABLE IF NOT EXISTS Student (First_Name TEXT, Middle_Name TEXT, Last_Name TEXT, Phone1 INTEGER, Phone2 INTEGER, Pin INTEGER, Current_Address TEXT, Permanent_Address TEXT, City TEXT, City_State TEXT,Gender TEXT, Area_of_intrest TEXT, Age INTEGER, Email TEXT, Suggession TEXT)')

    c.execute("INSERT INTO Student (First_Name,Middle_Name,Last_Name,Phone1,Phone2,Pin,Current_Address,Permanent_Address,City,City_State,Gender,Area_of_intrest,Age,Email,Suggession) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(Fname,Mname,Lname,Phone1,Phone2,Pin,Current_address,Permanent_address,City,State,Gender,Area_Of_Intrest,Age,Email,Suggession))
    connection.commit()
    
    
def Show_Data():
    c.execute('SELECT * FROM Student')
    views = c.fetchall()
    return views

