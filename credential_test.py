import unittest 
from credential import Credential

class TestCredential(unittest.TestCase):

    def setUp(self):
        self.new_credential = Credential("kirikabridgit@gmail.com","br254","nims67&")
        
    def test_unit(self):
        """
        this method tests if the credential is saved into the credentiallist
        """
        self.assertEqual(self.new_credential.Gmail,"kirikabridgit@gmail.com")
        self.assertEqual(self.new_credential.username,"br254")
        self.assertEqual(self.new_credential.password,"nims67&")


    def test_save_credential(self):
        """
        this method tests if the user object is saved in the credential list
        """
        self.new_credential.save_credential() # saves the new list
        self.assertEqual(len(Credential.credential_list),1)

    def test_save_multiple_credential(self):
        """
        checks if we can save multiple credentials
        """

        self.new_credential.save_credential()
        second_credential = Credential("Instagram","nimoh916","nims65$*")
        second_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)


    def tearDown(second_credential):
        """
        tearDown is a method that cleans up after each teat runs.
        """
        Credential.credential_list = []

    def test_find_credential_by_username(self):
        """
        method checks if we can find a credential by username
        """

        second_credential = Credential("Instagram","nimoh916","nims65$*")
        second_credential.save_credential()

        found_credential = Credential.find_credential_by_username("nimoh916")
        self.assertEqual(found_credential.username,second_credential.username)









if __name__ == '__main__':
    unittest.main()




