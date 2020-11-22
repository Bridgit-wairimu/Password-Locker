#!/usr/bin/env python
from password import User
from credential import Credential

def create_new_user(fname,lname,password):
    """
    function to create a new user
    """
    new_user = User(fname,lname,password)
    return new_user

def save_users(user):
    """
    function to save user
    """
    user.save_user()

def del_user(user):
    """
    function to delete a user
    """
    user.delete_user()

def find_user(password):
    """
    function that finds a user by password and returns the user
    """
    return User.find_user_by_password(password)

def check_existing_user(password):
    """
    function that check if a user exists with that a password return a boolean
    """
    return User.user_exist(password)

    if __name__ == '__main__':
        password()           
            




