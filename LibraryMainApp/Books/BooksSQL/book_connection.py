import sqlite3

# connect to database
conn = sqlite3.connect("../../../library.db")

# create a cursor/ pointer to the database
c = conn.cursor()

# get avalibility of the books
def getavailbility():
    ava = c.execute("SELECT Book_Name,Available_Copies FROM book")
    print(ava.fetchall())


getavailbility()

