import sqlite3

# connect to database for good purpose
conn = sqlite3.connect("../../../library.db")

# create a cursor/ pointer to the database
c = conn.cursor()
def Update_Column(M_name,Books_lended,Contact_No,DateOfJoining,MembersId ):
    c.execute('''UPDATE Members SET Member name =?,Books_lended =?,Contact_No=?,DateOfJoining  = ? WHERE  MembersId = ?''',(M_name,Books_lended,Contact_No,DateOfJoining,MembersId))
    conn.commit()

#Fetch history of user from lending using user id

def getByUserId(MemberId):
    c.execute("SELECT * FROM Lending WHERE MemberId =?",(MemberId,))
    history = c.fetchall()
    return  tuple(history)