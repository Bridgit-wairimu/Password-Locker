class Credential:
    """
    a class that generates new instances of credentials
    """

    credential_list= []
    
    def __init__(self,Gmail,username,password):
        """
        _init_ a method that helps to define properties for our objects.
        """
        self.Gmail = Gmail
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
