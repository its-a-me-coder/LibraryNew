import sqlite3

# connect to database for good purpose
conn = sqlite3.connect("../../../library.db")

# create a cursor/ pointer to the database
c = conn.cursor()


# update the quantity of books available

def update_available_quantity(field_values):
    c.execute('''UPDATE Book SET Book_ID =?,Available_Copies = ?  WHERE  Book_ID = ?''',(field_values[0],field_values[2],field_values[1]))
    conn.commit()


def add_books(id,name,total,available,genre,author,edition):
    c.execute("""INSERT INTO BOOK (Book_ID, Book_Name, Total_Copies,Available_Copies, Genre, Author_Name, Edition)
     VALUES(?,?,?,?,?,?,?, (id,name,total,available,genre,author,edition)""")
