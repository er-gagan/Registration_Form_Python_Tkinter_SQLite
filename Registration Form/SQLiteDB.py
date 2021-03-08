import sqlite3

connection = sqlite3.connect('student_database.sqlite')
c = connection.cursor()

def SendDB(Fname,Phone1,Gender,Age,Pin,Current_address,Permanent_address,City,State,Area_Of_Intrest,Suggession):
    
    c.execute('CREATE TABLE IF NOT EXISTS Student (First_Name TEXT, Phone1 INTEGER, Gender TEXT, Age INTEGER, Pin INTEGER, Current_Address TEXT, Permanent_Address TEXT, City TEXT, State TEXT, Area_of_intrest TEXT, Suggession TEXT)')

    c.execute("INSERT INTO Student (First_Name,Phone1,Gender,Age,Pin,Current_Address,Permanent_Address,City,State,Area_of_intrest,Suggession) VALUES (?,?,?,?,?,?,?,?,?,?,?)",(Fname,Phone1,Gender,Age,Pin,Current_address,Permanent_address,City,State,Area_Of_Intrest,Suggession))
    connection.commit()

    
def Show_Data():
    c.execute('SELECT * FROM Student')
    views = c.fetchall()
    return views

def DbClose():
    c.close()
    connection.close()