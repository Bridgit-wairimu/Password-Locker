#!/usr/bin/env python
from password import User, Credential

def create_new_user(fname,lname,password):
    """
    function to create a new user
    """
    new_user = User(fname,lname,password)
    return new_user

def save_user(user):
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

def display_user():
    """
    function to display user
    """
    return user.display_user()

def create_new_credential(Account,username,password):
    """
    function that creates new credential for a given user account
    """

    new_credential = Credential(Account,username,password)
    return new_credential

def save_credential(credential):
    """
    function to save credential 
    """

    credential.save_credential()

def delete_credential(credential):
    """
    function to delete a credential
    """
    credential.delete_credential()

def find_credential_by_username(username):
    """
    function that finds a user by password and returns the credential
    """
    return credential.find_credential_by_username(username)

def credential_exists(account):
    """
    Function that check if a Credentials exists with that account name and return true or false
    """
    return Credential.if_credential_exists(account)


def generate_password():
    '''
    generates a random password for the user.
    '''
    auto_password=credential.generatepassword()
    return auto_password
      

def main():
    print("Hello Welcome to your user list \n Please enter one of the following to proceed.\n CA ---  Create New Account  \n LI ---  Have An Account  \n")
    short_code=input("").lower()
    if short_code == "ca":
        print("Sign Up")
        print('*' * 50)
        username = input("User_name: ")

        while True:
            print(" TP - To type your own pasword:\n GP - To generate random Password")
            password_Choice = input().lower()
            if password_Choice== 'tp':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'gp':
                password = generate_password()
                break
            else:
                print("Invalid password please try again")

        save_user(create_new_user(first_name,last_name,password))
        print("*"*10)
        print(f"Hello {first_name} {last_name}, Your account has been created succesfully! Your password is: {password}")
        print("*"*10)

    while True:
        print("Use these short codes:\n cc - Create a new credential \n dc - Display Credentials \n  - Find a credential \n gp - Generate A randomn password \n d - Delete credential \n ex- Exit the application \n")
        short_code = input().lower()
        if short_code == "cc":
            print("Create New Credential")
            print("."*20)
            print("Account name ....")
            account = input().lower()
            print("Your Account username")
            username = input()

            while True:
                print(" TP - To type your own pasword if you already have an account:\n GP - To generate random Password")
                password_Choice = input().lower()
                if password_Choice == 'tp':
                    password = input("Enter Your Own Password\n")
                    break
                elif password_Choice == 'gp':
                    password = generate_password()
                    break
                else:
                    print("Invalid password please try again")

        
            save_credential(create_new_credential(Account,username,password))
            print('\n')
            print(f"Account Credential for: {Account} - username: {username} - password:{password} created succesfully")
            print('\n')

        elif short_code == "dc":
            if display_all_credential():
                print("Here's your list of accounts: ")
                 
                print('*' * 30)
                print('_'* 30)
                for account in display_all_credential():
                    print(f" Account:{Account.Account} \n User Name:{username}\n Password:{password}")
                    print('_'* 30)
                print('*' * 30)
            else:
                print("You don't have any credentials saved yet..........")

        elif short_code == "fc":
            print("Enter the account name you want to search for")
            search_name = input().lower()
            if find_credential_by_username(search_name):
                search_credential = find_credential_by_username(search_name)
                print(f"account name : {search_credential.Account}")
                print('-' * 50)
                print(f"user name: {search_credential.username} Password :{search_credential.password}")
                print('-' * 50)

            else:
                print("That Credential does not exist")
                print('\n')

        elif short_code == "d":
            print("Enter the account name of the Credential you want to delete")
            search_name = input().lower()
            if find_credential_by_username(search_name):
                search_credential = find_credential_by_username(search_name)
                print("_"*50)
                search_credential.delete_credential()
                print('\n')
                print(f"Your stored credentials for : {search_credential.Account} successfully deleted!!!")
                print('\n')
            else:
                print("That Credential you want to delete does not exist in your store yet")

        elif short_code == 'gp':

            password = generate_password()
            print(f" {password} Has been generated succesfull. You can proceed ")
        elif short_code == 'ex':
            print("Thanks for using passlocker have a nice day")
            break
        else:
            print("Wrong entry... Check your entry again and let it match those in the menu")
    else:
        print("Please enter a valid input to continue")

    
if __name__ == '__main__':
    main()