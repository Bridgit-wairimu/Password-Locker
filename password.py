
class User:
    """
    a class that generates new instances of passwors
    """

    user_list = []

    def __init__(self,first_name,last_name,password):
        """
        _init_ a method that helps to define properties for our objects.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_user(self):
         """
         this method saves contact objects into user_list
         """

         User.user_list.append(self)   

    @classmethod
    def find_user_by_password(cls,password):
        """
        this method takes in a password and returns a password that matches tha password.
        """

        for user in cls.user_list:
            if user.password == password:
                return user


    def delete_user(self):
        """
        this method deletes a user from the user_list
        """

        User.user_list.remove(self)

    @classmethod
    def user_exists(cls,password):
        """
        this method checks if a user exists fro the user_list
        """
        for user in cls.user_list:
            if user.password == password:
                return True

        return False

    @classmethod
    def display_user(cls):
        """
        this method returns the user list
        """
        return cls.user_list

    

class Credential:
    """
    a class that generates new instances of credentials
    """

    credential_list= []
    
    def __init__(self,Account,username,password):
        """
        _init_ a method that helps to define properties for our objects.
        """
        self.Gmail = Account
        self.username = username
        self.password = password


    def save_credential(self):
        """
        saves credentail objects into credential list
        """
        Credential.credential_list.append(self)

        
    @classmethod
    def find_credential_by_username(cls,username):
        """
        this method takes in username and returns a username that matches the username
        """
        for credential in cls.credential_list:
            if credential.username == username:
                return credential


    def delete_credential(self):
        """
        this method deletes a credential from the credentila_list
        """
        Credential.credential_list.remove(self)


    @classmethod 
    def credential_exists(cls,username):
        """
        this method checks if a credential exists fro the credential_list
        """
        for credential in cls.credential_list:
            if credential.username == username:
                return True

        return False 


    @classmethod
    def display_credential(cls):
        """
        this method returns the credential  list
        """
        return cls.credential_list



        
