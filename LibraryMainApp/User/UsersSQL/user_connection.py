import sqlite3

# connect to database for good purpose
conn = sqlite3.connect("../../../library.db")

# create a cursor/ pointer to the database
c = conn.cursor()

def Update_Contact(MembersId, Contact_No):
    c.execute('''UPDATE Members SET Contact_No = ?  WHERE  MembersId = ?''', (Contact_No, MembersId))
    conn.commit()

