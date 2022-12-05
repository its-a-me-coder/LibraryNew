from LibraryMainApp.User.UsersSQL.user_connection import *

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


