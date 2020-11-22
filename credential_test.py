import unittest 
from credential import Credential

class TestCredential(unittest.TestCase):

    def setUp(self):
        self.new_credential = credential("kirikabridgit@gmail.com","br254","nims67&")
        
    def test_unit(self):
        """
        this method tests if the credential is saved into the credentiallist
        """
        self.assertEqual(self.new_credential.Gmail,"kirikabridgit@gmail.com")
        self.assertEqual(self.new_credential.username,"br254")
        self.assertEqual(self.new_credential.password,"nims67&")


if __name__ == '__main__':
    unittest.main()




