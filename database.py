import sqlite3
conn=sqlite3.connect('Python_ATM.db')
c=conn.cursor()
c.execute("select * from Customer_file")
a=c.fetchall()
print(a)
