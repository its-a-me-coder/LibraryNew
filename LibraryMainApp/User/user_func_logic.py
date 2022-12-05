from LibraryMainApp.Books.BooksSQL.book_connection import *

# Adding books to library

def Add_Book_to_Library():
    name = input("Enter the Name of the Book: ")
    total = int(input("Enter total Number of Books: "))
    available = int(input("Enter Number of books Available: "))
    genre = input("Enter Genre: ")
    author = input("Enter the Author Name: ")
    edition = input("Enter the Edition: ")
    add_books(name,total,available,genre,author,edition)

Add_Book_to_Library()

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

Update_Books_to_Library()