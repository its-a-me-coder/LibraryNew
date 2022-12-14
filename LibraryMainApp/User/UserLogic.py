from LibraryMainApp.User.UsersSQL.user_connection import *
from LibraryMainApp.Books.BooksSQL.book_connection import *
def login():
    """Creating login function if user not present in table add user"""
    user_id = input("Enter user id: ")
    user_name = input("Enter user name: ")

    if checkMember(user_id, user_name) is not None:
        return user_id
    else:
        print("user not found creating new user")
        newUserName = input("enter name: ")
        newUserContact = input("enter contact number: ")
        newUserId = add_members(newUserName,newUserContact)
        print(f"Uesr add user name: {newUserName} and user id: {newUserId[0]}")
        return newUserId[0]



USERID = 1  # This is the user id that we get from the login
"\" Got this from the user login page "
from tabulate import tabulate


def show_books_in_library():
    """This function shows the books in the library"""
    books = get_book_names()
    print(tabulate(books, headers=['Book Name', 'Author', 'Edition', 'Genre']))
    print("Enter 1 to go back to the menu")


def show_books_borrowed():
    """This function shows the books borrowed by the user"""
    books = tuple(getByUserId(1))
    print(books)


def return_book(bookid):
    """This function returns the book"""
    book_current_available = int(get_book_quantity(bookid))  # checks the current available quantity of the book
    user_books_lent = getbooklended(USERID)  # gets the amount of books lent by the user
    check, LentID = checkif_lent(bookid, USERID)
    if user_books_lent <= 0 or check == False:  # checks if the user has lent the book
        print("You have not borrowed this book or you have not borrowed any book")
        return False
    else:
        updatebooklended(USERID, user_books_lent - 1)  # updates the amount of books lent by the user
        update_available_quantity(bookid, book_current_available + 1)  # updates the available quantity of the book
        delete_lent(LentID)  # deletes the record of the book lent
        print("Book Returned")  # prints that the book  is returned
        print("Enter 1 to go back to the menu")
    return True

def lending_book(bookid):
    """ This function is for lending a book from the library """


def Update_ContactNo(memberid, Contact_info):
    """This function updates the information about the members"""
    Update_Contact(memberid, Contact_info) # updates the new information into the previous one.
    print("New Updates have been done!, The contact now is:",Contact_info)
    return True

# Try to lend a book from the library ( using id or name and check avail. )
def lendBook(bookid):
    book_current_available = int(get_book_quantity(bookid))  # checks the current available quantity of the book
    user_books_lent = getbooklended(USERID)  # gets the amount of books lent by the user
    check, LentID = checkif_lent(bookid, USERID)
    if user_books_lent >= 3 or check == True:  # checks if the user has lent the book
        print("You have reached the maximum books you can borrow or you have already lended this book")
        return False
    else:
        updatebooklended(USERID, user_books_lent + 1)  # updates the amount of books lent by the user
        update_available_quantity(bookid, book_current_available - 1)  # updates the available quantity of the book
        lendid= Book_Issued(bookid,USERID)  # deletes the record of the book lent
        print("Book issued with lending id",lendid[0])  # prints that the book  is returned
        print("Enter 1 to go back to the menu")
    return True


# Adding books to library

def Add_Book_to_Library():
    name = input("Enter the Name of the Book: ")
    total = int(input("Enter total Number of Books: "))
    available = int(input("Enter Number of books Available: "))
    genre = input("Enter Genre: ")
    author = input("Enter the Author Name: ")
    edition = input("Enter the Edition: ")
    add_books(name,total,available,genre,author,edition)

# Updating the details of the books in the library

def Update_Books_to_Library():
    Root_ID = int(input("Enter the Root Id: "))
    id = int(input("Enter the Book ID:"))
    Name = input("Enter the name of the Book: ")
    Total = int(input("Enter the total Number of Books: "))
    Available = int(input("Enter the available number of Books: "))
    genre = input("Enter the Genre: ")
    Aname = input("Enter the Author Name: ")
    Ed = input("Enter the Edition: ")
    Update_Column(Root_ID,id,Name,Total,Available,genre,Aname,Ed)



def Add_Book_to_Library():
    """This function adds a book to the library"""
    name = input("Enter the Name of the Book: ")
    total = int(input("Enter total Number of Books: "))
    available = int(input("Enter Number of books Available: "))
    genre = input("Enter Genre: ")
    author = input("Enter the Author Name: ")
    edition = input("Enter the Edition: ")
    add_books(name,total,available,genre,author,edition)

def Update_Books_to_Library():
    """This function updates the books in the library"""
    Root_ID = int(input("Enter the Root Id: "))
    id = int(input("Enter the Book ID:"))
    Name = input("Enter the name of the Book: ")
    Total = int(input("Enter the total Number of Books: "))
    Available = int(input("Enter the available number of Books: "))
    genre = input("Enter the Genre: ")
    Aname = input("Enter the Author Name: ")
    Ed = input("Enter the Edition: ")
    Update_Column(Root_ID,id,Name,Total,Available,genre,Aname,Ed)




