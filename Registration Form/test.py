import sqlite3

connection = sqlite3.connect('h.sql')
c = connection.cursor()
Fname="Gagan kkr"
Lname="Aggarwal nhj"
c.execute('CREATE TABLE IF NOT EXISTS Student (First_Name TEXT, Last_Name TEXT)')

c.execute("INSERT INTO Student (First_Name,Last_Name) VALUES (?,?)",(Fname,Lname))
connection.commit()

c.close()
connection.close()