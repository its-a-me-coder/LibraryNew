import sqlite3

# connect to database for good purpose
conn = sqlite3.connect("../../../library.db")

# create a cursor/ pointer to the database
c = conn.cursor()

# get all the details of all the users
def display_Details():
    details = c.execute("SELECT * from USER")
    return(details)

# add a row to lend whenever a book is issued
def Book_Issued(LendId, BookId, MemberId):
    c.execute('SELECT date("now")')
    x = c.fetchall()
    a = x[0]
    DateOfIssue = str(a[0])
    c.execute('SELECT date("now","+10 days")')
    y = c.fetchall()
    b = y[0]
    DateOfReturn = str(b[0])
    User_Issued_Book = c.execute("INSERT OR IGNORE INTO Lending (LendId, BookId, MemberId, DateOfIssue, DateOfReturn) VALUES(?,?,?,?,?) ",(LendId, BookId, MemberId, DateOfIssue, DateOfReturn))
    conn.commit()



