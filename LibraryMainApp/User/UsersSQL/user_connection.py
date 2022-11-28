import sqlite3

# connect to database for good purpose
conn = sqlite3.connect("../../../library.db")

# create a cursor/ pointer to the database
c = conn.cursor()

#get books lended to the user
def getbooklended(MemId):
    c.execute("SELECT Books_Lended FROM Members WHERE MembersId=?",(MemId,))
    booklended = c.fetchall()
    return tuple(booklended)

