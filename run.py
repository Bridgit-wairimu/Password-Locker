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

def del_credential(credential):
    """
    function to delete a credential
    """
    credential.credential_user()

def find_credential(username):
    """
    function that finds a user by password and returns the credential
    """
    return credential.find_credential_by_username(username)

def display_credential():
    """
    function to display credential
    """
    return credential.display_credential()


def generate_Password():
    '''
    generates a random password for the user.
    '''
    auto_password=Credential.generatePassword()
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
            password_Type = input().lower().strip()
            if password_Type== 'tp':
                password = input("Enter Password\n")
                break
            elif password_Type == 'gp':
                password = generate_Password()
                break
            else:
                print("Invalid password please try again")

        save_user(create_new_user(fname,lname,password))
        print("*"*85)
        print(f"Hello {username}, Your account has been created succesfully! Your password is: {password}")
        print("*"*85)

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
                    password = generate_Password()
                    break
                else:
                    print("Invalid password please try again")
                elif shortcode == 'du':
                    if display_user():
                        print("Here is a list of all your users")
                        for user in display_user():
                            print(f"{user.first_name} {user.lastname} .. {user.password}")
                            print('/n')
                else:
                    print('/n')
                    print("you don't have any user stored yet")
                    print('/n')
                else short_code == 'fu'
                print("enter the username you want to search for")
                 search_username = input()
                 if check_existing_user(search_username)
                    search_user = find_user(search_username)
                    print(f"{search_user.fisrt_name} {search_user.last_name}")
                    print('_' * 20)

                    print(f"password....{search_user.password}")

                else:
                    print("that user does not exist")    


            save_credential(create_new_credential(account,username,password))
            print('\n')
            print(f"Account Credential for: {account} - username: {username} - password:{password} created succesfully")
            print('\n')

        elif short_code == "dc":
            if display_credential():
                print("Here's your list of acoounts: ")
                 
                print('*' * 30)
                print('_'* 30)
                for account in display_credential():
                    print(f" Account:{account.account} \n User Name:{username}\n Password:{password}")
                    print('_'* 30)
                print('*' * 30)
            else:
                print("You don't have any credentials saved yet..........")

        elif short_code == "fc":
            print("Enter the account name you want to search for")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"account Name : {search_credential.Account}")
                print('-' * 50)
                print(f"user Name: {search_credential.username} Password :{search_credential.password}")
                print('-' * 50)

            else:
                print("That Credential does not exist")
                print('\n')

        elif short_code == "d":
            print("Enter the account name of the Credential you want to delete")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("_"*50)
                search_credential.delete_credential()
                print('\n')
                print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                print('\n')
            else:
                print("That Credential you want to delete does not exist in your store yet")

        elif short_code == 'gp':

            password = generate_Password()
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