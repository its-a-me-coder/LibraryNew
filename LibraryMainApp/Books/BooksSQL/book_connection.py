import sqlite3

# connect to database for good purpose
conn = sqlite3.connect("../../library.db")

# create a cursor/ pointer to the database
c = conn.cursor()


def getavailbility(book_id):
    """Get the details of a book latest interaction using book id"""
    c.execute("SELECT Available_Copies FROM book WHERE Book_ID=?", (book_id,))
    rec = c.fetchall()
    return tuple(rec)


def getByGenre(gen):
    """Get the details of a book latest interaction using book id"""
    book_genre = c.execute("SELECT Book_Name,Author_Name,Edition FROM Book WHERE Genre=?", (gen,))
    return tuple(book_genre)


# deleteBook
def deleteBook(del_id):
    """Delete a book from the table"""
    c.execute("DELETE FROM Book WHERE Book_id =?", (del_id,))


def get_book_quantity(book_id):
    """Get the details of a book latest interaction using book id"""
    c.execute("SELECT Available_Copies FROM book WHERE Book_ID=?", (book_id,))
    rec = c.fetchall()
    return tuple(rec)[0][0]


def update_available_quantity(bookid, available):
    """Update the column book lent of the table"""
    c.execute('''UPDATE Book SET Available_Copies = ?  WHERE  Book_ID = ?''', (bookid, available))


def update_available_quantity(bookid, available):
    """Update the column book lent of the table"""
    c.execute('''UPDATE Book SET Available_Copies = ?  WHERE  Book_ID = ?''', (available, bookid))

    conn.commit()


def get_book_names():
    """Get the details of  books"""
    book_names = c.execute("SELECT Book_Name,Author_Name,Edition,Genre FROM Book ")
    return tuple(book_names)


def update_total_quantity(bookid, total):
    """Update the column book total copies of the table"""
    c.execute('''UPDATE Book SET Total_Copies = ?  WHERE  Book_ID = ?''', (total, bookid))
    conn.commit()


def add_books( name, total, available, genre, author, edition):
    """Add a book to the table"""
    c.execute("""INSERT INTO BOOK (Book_Name, Total_Copies,Available_Copies, Genre, Author_Name, Edition)
     VALUES(?,?,?,?,?,?)""", (name, total, available, genre, author, edition))
    conn.commit()


def getByAuthor(Aut):
    """Get the details of a book  using author name"""
    book_author = c.execute("SELECT Book_Name,Author_Name,Edition FROM Book WHERE Author_Name=?", (Aut,))
    return tuple(book_author.fetchall())


def Update_Column(Root_ID, id, Name, Total, Available, genre, Aname, Ed):
    """Update the column of the table"""
    c.execute(
        '''UPDATE Book SET Book_ID =?,Book_Name =?, Total_Copies=?, Available_Copies = ?,Genre=?,Author_Name=?,
        Edition=?  WHERE  Book_ID = ?''',
        (id, Name, Total, Available, genre, Aname, Ed, Root_ID))
    conn.commit()
