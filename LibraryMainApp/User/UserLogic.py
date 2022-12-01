from LibraryMainApp.User.UsersSQL.user_connection import *
from LibraryMainApp.Books.BooksSQL.book_connection import *

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
    return True


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
