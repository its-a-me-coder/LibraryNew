import sqlite3

# connect to database for good purpose
conn = sqlite3.connect("../../../library.db")

# create a cursor/ pointer to the database
c = conn.cursor()

# Deletes a member using member id
def delete_member(mem_id):
    c.execute("DELETE FROM Members WHERE MembersId =?", (mem_id,))

# Gives all the records of a particular book
def history_book(book_id):
    c.execute("SELECT * FROM Lending WHERE BookId=?", (book_id,))
    return tuple(c.fetchall())

