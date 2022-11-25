import sqlite3

# connect to database
conn = sqlite3.connect("../../../library.db")

# create a cursor/ pointer to the database
c = conn.cursor()

# get avalibility of the books
def getavailbility():
    c.execute("SELECT Book_Name,Available_Copies FROM book")
    rec = c.fetchall()
    ava = [x[1] for x in rec]
    book = [x[0] for x in rec]
    for i in range(len(book)-1):
        print(f" {book[i]}, availability : {ava[i]}")


getavailbility()

