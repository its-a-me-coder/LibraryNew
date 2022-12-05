from LibraryMainApp.User.UserLogic import *
from LibraryMainApp.Books.BooksSQL.book_connection import *

print("Welcome to Library management system")

def Librarian():
    '''all the function related to librarian are here'''
    while True:
        print(" Hi librarian, welcome to your desk.")
        print(" Press 1 to add a new book to the library")
        print(" Press 2 to show the total collection of books available ")
        print(" Press 3 to remove a book from the library ")
        print(" Press 4 to update any book ")
        print(" Press 5 to Quit")

        a=int(input("enter ur choice: "))
        if a==1:
            '''func to add book in library'''
            Add_Book_to_Library()
            print("1")

        elif a==2:
            '''func show books in library'''
            print("2")
            print(get_book_names())

        elif a==3:
            '''func to delete a book from library'''
            print("3")
            book_id=input("enter book id to be deleted")
            deleteBook(book_id)

        elif a==4:
            '''update any book'''
            Update_Books_to_Library()
            print("4")

        elif a==5:
            '''Quit'''
            print("5")
            break

        else:
            print("Enter correct option")


while True:
    '''present user with option to choose between member and librarian'''
    n = int(input("Press 1 for user or press 2 for Librarian: "))
    if n==1:
        User_id=login()
        break
    elif (n==2):
        user_id=login()
        Librarian()
        break
    else:
        print("enter correct value")




