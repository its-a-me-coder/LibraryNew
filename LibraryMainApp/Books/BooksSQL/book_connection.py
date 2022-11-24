import sqlite3

# connect to database
conn = sqlite3.connect("../../../library.db")

# create a cursor/ pointer to the database
c = conn.cursor()

c.execute("""SELECT book_name FROM book
""")
print(c.fetchall())
