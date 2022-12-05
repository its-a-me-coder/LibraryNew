import sqlite3

conn = sqlite3.connect("../../Library.db")  # connect to database for testing purpose

# create a cursor/ pointer to the database
cursor = conn.cursor()
from datetime import date,timedelta

def Update_Column(M_name, Books_lended, Contact_No, DateOfJoining, MembersId):
    """Update the column of the table"""
    cursor.execute(
        '''UPDATE Members SET Member name =?,Books_lended =?,Contact_No=?,DateOfJoining  = ? WHERE  MembersId = ?''',
        (M_name, Books_lended, Contact_No, DateOfJoining, MembersId))
    conn.commit()


# Fetch history of user from lending using user id

def getByUserId(MemberId):
    """Get the details of a users latest interaction using user id"""
    cursor.execute("SELECT * FROM Lending WHERE MemberId =?", (MemberId,))
    history = cursor.fetchall()
    print(tuple(history))
    return tuple(history)


# get books lended to the user

def getbooklended(MemId):
    """Get the details of books lent by a user using user id"""
    cursor.execute("SELECT Books_Lended FROM Members WHERE MembersId=?", (MemId,))
    booklended = cursor.fetchall()
    return tuple(booklended)[0][0]


def checkif_lent(BookId, MembersId):
    """Check if a book is actually lent to a user"""
    cursor.execute("SELECT LendId FROM Lending WHERE BookId =? AND MemberId =?", (BookId, MembersId))
    lent = cursor.fetchall()
    if lent == []:
        return (False, None)
    else:
        return True, lent[0][0]


def updatebooklended(MembersId, Books_Lended):
    """Update the column book lent of the table"""
    cursor.execute('''UPDATE Members SET Books_Lended = ?  WHERE  MembersId = ?''', (Books_Lended, MembersId))
    conn.commit()


def delete_member(mem_id):
    """Delete a member from the table"""
    cursor.execute("DELETE FROM Members WHERE MembersId =?", (mem_id,))


def history_book(book_id):
    """Get the details of a book latest interaction using book id"""
    cursor.execute("SELECT * FROM Lending WHERE BookId=?", (book_id,))
    return tuple(cursor.fetchall())


# addition of members


def add_members(Name, contact):
    """Add a member to the table"""
    cursor.execute('SELECT date("now")')
    x = cursor.fetchall()
    DateOfjoining = str(x[0])
    cursor.execute("""INSERT INTO Members ('Member Name', Books_Lended,Contact_No, DateOfJoining) VALUES(?,?,?,?) """,
                   (Name, 0, contact, DateOfjoining))
    conn.commit()
    return cursor.execute("SELECT MembersId FROM Members ORDER BY MembersId DESC ").fetchone()


def Update_Contact(MembersId, Contact_No):
    """Update the column contact of the table"""
    cursor.execute('''UPDATE Members SET Contact_No = ?  WHERE  MembersId = ?''', (Contact_No, MembersId))
    conn.commit()


# get all the details of all the users
def display_Details():
    """Get the details of all the users"""
    details = cursor.execute("SELECT * from USER").fetchall()
    return (details)


def delete_lent(LendId):
    """Delete a row from the table lending"""
    cursor.execute("DELETE FROM Lending WHERE LendId =?", (LendId,))
    conn.commit()


# add a row to lend whenever a book is issued
def Book_Issued(BookId, MemberId):
    """Add a row to lend whenever a book is issued"""
    IssuedDate = date.today()
    DateOfIssue = IssuedDate.strftime("%d/%m/%Y")
    ReturnDate = IssuedDate + timedelta(days=14)
    User_Issued_Book = cursor.execute(
        "INSERT OR IGNORE INTO Lending ( BookId, MemberId, DateOfIssue, DateOfReturn) VALUES(?,?,?,?) ",
        (BookId, MemberId, DateOfIssue, ReturnDate))
    conn.commit()


def checkMember(user_id, user_name):
    '''checking member in table or not'''
    return cursor.execute("SELECT MembersId FROM Members WHERE MembersId=? and `Member Name` =?",
                          (user_id, user_name)).fetchone()
