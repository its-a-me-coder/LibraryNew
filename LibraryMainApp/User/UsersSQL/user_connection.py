import sqlite3

# connect to database for good purpose
conn = sqlite3.connect("../../library.db")

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



#get books lended to the user
def getbooklended(MemId):
    c.execute("SELECT Books_Lended FROM Members WHERE MembersId=?",(MemId,))
    booklended = c.fetchall()
    return tuple(booklended)


# Deletes a member using member id
def delete_member(mem_id):
    c.execute("DELETE FROM Members WHERE MembersId =?", (mem_id,))

# Gives all the records of a particular book
def history_book(book_id):
    c.execute("SELECT * FROM Lending WHERE BookId=?", (book_id,))
    return tuple(c.fetchall())


# addition of members

def add_members(Name, contact):
    c.execute('SELECT date("now")')
    x = c.fetchall()
    DateOfjoining = str(x[0])
    c.execute("""INSERT INTO Members ('Member Name', Books_Lended,Contact_No, DateOfJoining) VALUES(?,?,?,?) """,
              (Name, 0, contact, DateOfjoining))
    conn.commit()
    return c.execute("SELECT MembersId FROM Members ORDER BY MembersId DESC ").fetchone()

def Update_Contact(MembersId, Contact_No):
    c.execute('''UPDATE Members SET Contact_No = ?  WHERE  MembersId = ?''', (Contact_No, MembersId))
    conn.commit()





# get all the details of all the users
def display_Details():
    details = c.execute("SELECT * from USER")
    return(details)

# add a row to lend whenever a book is issued
def Book_Issued(LendId, BookId, MemberId):
    c.execute('SELECT date("now")')
    x = c.fetchall()
    a = x[0]
    DateOfIssue = str(a[0])
    c.execute('SELECT date("now","+10 days")')
    y = c.fetchall()
    b = y[0]
    DateOfReturn = str(b[0])
    User_Issued_Book = c.execute("INSERT OR IGNORE INTO Lending (LendId, BookId, MemberId, DateOfIssue, DateOfReturn) VALUES(?,?,?,?,?) ",(LendId, BookId, MemberId, DateOfIssue, DateOfReturn))
    conn.commit()

def checkMember(user_id,user_name):
    return c.execute("SELECT MembersId FROM Members WHERE MembersId=? and `Member Name` =?", (user_id, user_name)).fetchone()








