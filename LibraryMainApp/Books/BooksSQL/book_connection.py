import sqlite3

# connect to database
conn = sqlite3.connect("../../../library.db")

# create a cursor/ pointer to the database
c = conn.cursor()

c.execute("""SELECT book_name FROM book
""")
print(c.fetchall())

#getByGenre
def getByGenre():
    gen = 'Fiction'
    book_genre=c.execute("SELECT Book_Name,Author_Name,Edition FROM Book WHERE Genre=?",(gen,))
    print(book_genre.fetchall())

#deleteBook
def deleteBook():
    del_id=1
    c.execute("DELETE FROM Book WHERE Book_id =?",(del_id,))
    after_del=c.execute("SELECT * FROM Book")
    print(after_del.fetchall())

getByGenre()
deleteBook()