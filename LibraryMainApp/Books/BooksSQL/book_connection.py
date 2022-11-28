import sqlite3

# connect to database
conn = sqlite3.connect("../../../library.db")

# create a cursor/ pointer to the database
c = conn.cursor()

# get avalibility of the books
def getByAuthor(Aut):
    book_author=c.execute("SELECT Book_Name,Author_Name,Edition FROM Book WHERE Author_Name=?",(Aut,))
    return tuple(book_author.fetchall())




def Update_Column(Root_ID, id,Name, Total, Available, genre, Aname, Ed):
    c.execute('''UPDATE Book SET Book_ID =?,Book_Name =?, Total_Copies=?, Available_Copies = ?,Genre=?,Author_Name=?,Edition=?  WHERE  Book_ID = ?''',(id,Name, Total, Available, genre, Aname, Ed, Root_ID))
    conn.commit()



