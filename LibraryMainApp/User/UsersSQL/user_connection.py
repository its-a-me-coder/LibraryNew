import sqlite3

# connect to database for good purpose
conn = sqlite3.connect("../../Library.db")  # connect to database for testing purpose
# create a cursor/ pointer to the database
cursor = conn.cursor()


def Update_Column(M_name, Books_lended, Contact_No, DateOfJoining, MembersId):
    cursor.execute(
        '''UPDATE Members SET Member name =?,Books_lended =?,Contact_No=?,DateOfJoining  = ? WHERE  MembersId = ?''',
        (M_name, Books_lended, Contact_No, DateOfJoining, MembersId))
    conn.commit()


# Fetch history of user from lending using user id

def getByUserId(MemberId):
    cursor.execute("SELECT * FROM Lending WHERE MemberId =?", (MemberId,))
    history = cursor.fetchall()
    print(tuple(history))
    return tuple(history)


# get books lended to the user
def getbooklended(MemId):
    cursor.execute("SELECT Books_Lended FROM Members WHERE MembersId=?", (MemId,))
    booklended = cursor.fetchall()
    return tuple(booklended)[0][0]


def checkif_lent(BookId, MembersId):
    cursor.execute("SELECT LendId FROM Lending WHERE BookId =? AND MemberId =?", (BookId, MembersId))
    lent = cursor.fetchall()
    if lent == []:
        return (False,None)
    else:
        return (True, lent[0][0])


def updatebooklended(MembersId, Books_Lended):
    cursor.execute('''UPDATE Members SET Books_Lended = ?  WHERE  MembersId = ?''', (Books_Lended, MembersId))
    conn.commit()


# Deletes a member using member id
def delete_member(mem_id):
    cursor.execute("DELETE FROM Members WHERE MembersId =?", (mem_id,))


# Gives all the records of a particular book
def history_book(book_id):
    cursor.execute("SELECT * FROM Lending WHERE BookId=?", (book_id,))
    return tuple(cursor.fetchall())


# addition of members

def add_members(Name, booklended, cont):
    cursor.execute('SELECT date("now")')
    x = cursor.fetchall()
    DateOfjoining = str(x[0])

    cursor.execute("""INSERT INTO Members ('Member Name', Books_Lended,Contact_No, DateOfJoining) VALUES(?,?,?,?) """,
                   (Name, booklended, cont, DateOfjoining))

    conn.commit()


def Update_Contact(MembersId, Contact_No):
    cursor.execute('''UPDATE Members SET Contact_No = ?  WHERE  MembersId = ?''', (Contact_No, MembersId))
    conn.commit()


# get all the details of all the users
def display_Details():
    details = cursor.execute("SELECT * from USER")
    return (details)

def delete_lent(LendId):
    cursor.execute("DELETE FROM Lending WHERE LendId =?", (LendId,))
    conn.commit()
# add a row to lend whenever a book is issued
def Book_Issued(BookId, MemberId):
    cursor.execute('SELECT date("now")')
    x = cursor.fetchall()
    a = x[0]
    DateOfIssue = str(a[0])
    cursor.execute('SELECT date("now","+10 days")')
    y = cursor.fetchall()
    b = y[0]
    DateOfReturn = str(b[0])
    User_Issued_Book = cursor.execute(
        "INSERT OR IGNORE INTO Lending ( BookId, MemberId, DateOfIssue, DateOfReturn) VALUES(?,?,?,?) ",
        (BookId, MemberId, DateOfIssue, DateOfReturn))
    conn.commit()
    return cursor.execute("SELECT LendId FROM Lending ORDER BY LendId DESC ").fetchone()
