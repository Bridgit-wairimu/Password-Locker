#!/usr/bin/env python
from password import User, Credential

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

def display_user():
    """
    function to display user
    """
    return User.display_user()

def login_user(fname,lname,password):
     """
     function that checks whether a user exist and then the user logs in
     """

     check_user = Credential.verify_user(fname,lname,password)
     return check_user



def create_new_credential(Gmail,username,password):
    """
    function that creates new credential for a given user account
    """

    new_credential = Credential(Gmail,username,password)
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
      
def main():
    print("Hello welcome to your user list.What is your name?")
    user_name = input()


    print(f"Hello {user_name}.what would you like to do?")
    print('/n')

while True:
        print("Use these short codes : cc - create a new user, dc - display user, fc -find a user, ex -exit the user list ")
        short_code = input().lower()

        if short_code == 'ur':
            print("New User")
            print("_"*10)


            print ("First name....")
            f_name = input()

            print ("Last name....")
            l_name = input()

            print ("password....")
            password = input()

            save_user(create_user(f_name,l_name,password)) # create and save new user.

            print ('\n')
            print(f"New User {f_name} {l_name} created")
            print ('\n')


        elif short_code == 'du':

                            if display_user():
                                    print("Here is a list of all your users")
                                    print('\n')

                                    for contact in display_user():
                                            print(f"{user.first_name} {user.last_name} .....{contact.phone_number}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any users saved yet")
                                    print('\n')

        elif short_code == 'fu':

                            print("Enter the username you want to search for")

                            search_username = input()
                            if check_existing_user(search_username):
                                    search_user = find_user(search_username)
                                    print(f"{search_user.first_name} {search_user.last_name}")
                                    print('-' * 20)

                                    print(f"password.......{search_user.password}")
                            else:
                                    print("That user does not exist")

        elif short_code == "ex":
                print("Bye .......")
                break
        else:
                print("I really didn't get that. Please use the short codes")

        save_credential(create_credential(account,username,password)) # create and save new user.

        print ('\n')
        print(f"New Credential {account} {username} created")
        print ('\n')

        elif short_code == 'dc':

                            if display_credential():
                                    print("Here is a list of all your credential")
                                    print('\n')

                                    for contact in display_credential():
                                            print(f"{credential.first_name} {cred2ential.last_name} .....{contact.phone_number}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any credential saved yet")
                                    print('\n')

        elif short_code == 'fc':

                            print("Enter the username you want to search for")

                            search_username = input()
                            if check_existing_credential(search_username):
                                    search_credential = find_credential(search_username)
                                    print(f"{search_credential.username} {search_credential.account} ")
                                    print('-' * 20)

                                    print(f"password.......{search_user.password}")
                            else:
                                    print("That credential does not exist")

        elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")


    
if __name__ == '__main__':
    main()

    

