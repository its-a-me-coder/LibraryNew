import sqlite3

# connect to database for good purpose
conn = sqlite3.connect("../../../library.db")

# create a cursor/ pointer to the database
c = conn.cursor()


# addition of members

def add_members(Name, booklended, cont):
    c.execute('SELECT date("now")')
    x = c.fetchall()
    DateOfjoining = str(x[0])

    c.execute("""INSERT INTO Members ('Member Name', Books_Lended,Contact_No, DateOfJoining) VALUES(?,?,?,?) """,
              (Name, booklended, cont, DateOfjoining))

    conn.commit()

def Update_Contact(MembersId, Contact_No):
    c.execute('''UPDATE Members SET Contact_No = ?  WHERE  MembersId = ?''', (Contact_No, MembersId))
    conn.commit()

