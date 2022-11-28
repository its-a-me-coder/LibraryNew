import sqlite3

# connect to database
conn = sqlite3.connect("../../../library.db")

# create a cursor/ pointer to the database
c = conn.cursor()

# get avalibility of the books
def getavailbility(book_id):
    c.execute("SELECT Available_Copies FROM book WHERE Book_ID=?",(book_id,))
    rec = c.fetchall()
    return tuple(rec)


