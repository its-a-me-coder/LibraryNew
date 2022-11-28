import sqlite3

# connect to database
conn = sqlite3.connect("../../../library.db")

# create a cursor/ pointer to the database
c = conn.cursor()



#getByGenre
def getByGenre(gen):
    book_genre=c.execute("SELECT Book_Name,Author_Name,Edition FROM Book WHERE Genre=?",(gen,))
    return tuple(book_genre)

#deleteBook
def deleteBook(del_id):
    c.execute("DELETE FROM Book WHERE Book_id =?",(del_id,))



