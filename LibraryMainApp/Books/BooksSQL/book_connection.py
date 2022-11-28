import sqlite3

# connect to database for good purpose
conn = sqlite3.connect("../../../library.db")

# create a cursor/ pointer to the database
c = conn.cursor()

# get avalibility of the books
def getavailbility(book_id):
    c.execute("SELECT Available_Copies FROM book WHERE Book_ID=?",(book_id,))
    rec = c.fetchall()
    return tuple(rec)

#getByGenre
def getByGenre(gen):
    book_genre=c.execute("SELECT Book_Name,Author_Name,Edition FROM Book WHERE Genre=?",(gen,))
    return tuple(book_genre)

#deleteBook
def deleteBook(del_id):
    c.execute("DELETE FROM Book WHERE Book_id =?",(del_id,))

# update the quantity of books available

def update_available_quantity(field_values):
    c.execute('''UPDATE Book SET Book_ID =?,Available_Copies = ?  WHERE  Book_ID = ?''',(field_values[0],field_values[2],field_values[1]))
    conn.commit()

def get_book_names():
    book_names = c.execute("SELECT Book_Name,Author_Name,Edition,Genre FROM Book ")
    return tuple(book_names)


def update_total_quantity(bookid, total):
    c.execute('''UPDATE Book SET Total_Copies = ?  WHERE  Book_ID = ?''', (total, bookid))
    conn.commit()


def getByAuthor(Aut):
    book_author=c.execute("SELECT Book_Name,Author_Name,Edition FROM Book WHERE Author_Name=?",(Aut,))
    return tuple(book_author.fetchall())




def Update_Column(Root_ID, id,Name, Total, Available, genre, Aname, Ed):
    c.execute('''UPDATE Book SET Book_ID =?,Book_Name =?, Total_Copies=?, Available_Copies = ?,Genre=?,Author_Name=?,Edition=?  WHERE  Book_ID = ?''',(id,Name, Total, Available, genre, Aname, Ed, Root_ID))
    conn.commit()
