import sqlite3

# connect to database for good purpose
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



