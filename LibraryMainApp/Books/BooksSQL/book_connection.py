import sqlite3

# connect to database
conn = sqlite3.connect("../../../library.db")

# create a cursor/ pointer to the database
c = conn.cursor()

# get avalibility of the books
def getByAuthor():
    Aut = 'Britt Bennett'
    book_author=c.execute("SELECT Book_Name,Author_Name,Edition FROM Book WHERE Author_Name=?",(Aut,))
    print(book_author.fetchall())


getByAuthor()

def Update_Column():
    update_column=c.execute("ALTER TABLE Book ADD COLUMN phone VARCHAR(50)")
    book=c.execute("SELECT * FROM Book")
    print(book.fetchall())


Update_Column()