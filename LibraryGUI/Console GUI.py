
print("Welcome to Library management system")
print("Enter the coorect choice to proceed")
print("Are you an user or the librarian?")
n = int(input("Press 1 for user or press 2 for Librarian: "))
if n==1:
    print()
    n=int(input("If u are a member, please enter 1  else press 0"))
    if n!=0:
        '''search for member fucntion'''

        '''if member not found ask user to enter corerect id'''
    else:
        '''create a new member fucntion'''
elif (n==2):
    '''check if librareian is valid'''

    print(" Hi librarian, welcome to your desk.")
    print(" Press 1 to add a new book to the library")
    print(" Press 2 to show the total collection of books available ")
    print(" Press 3 to remove a book from the library ")
    print(" Press 4 to update any book ")

    a=int(input("enter ur choice: "))
    if a==1:
        '''func to add book in library'''
    elif a==2:
        '''func show books in library'''
    elif a==3:
        '''func to delete a book from library'''
    elif a==4:
        '''update any book'''
    else:
        print("Enter correct option")

