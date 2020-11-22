import unittest
from password import User

class TestPassword(unittest.TestCase):

    def setUp(self):
        self.new_user = User("bridgit","kirika","b243#$5")

    def test_init(self):
        self.assertEqual(self.new_user.first_name,"bridgit")
        self.assertEqual(self.new_user.last_name,"kirika")
        self.assertEqual(self.new_user.password,"b243#$5")


    def test_save_user(self):
            """
            this method tests if the user object is saved into the userlist
            """
            self.new_user.save_user() # saves the new user
            self.assertEqual(len(User.user_list),1)


    def test_save_multiple_user(self):
            """
            checks if we can save multiple users
            """

            self.new_user.save_user()
            second_user = User("kayleen","green","k2r$678") # new user
            second_user.save_user()
            self.assertEqual(len(User.user_list),2)

    def tearDown(second_user):
        """
        tearDown is a method that cleans up after each teat runs.
        """
        User.user_list = []

        
    def test_find_user_by_password(self):
            """
            method checks if we can find a user by password
            """

            self.new_user.save_user()
            second_user = User("kayleen","green","k2r$678") # new user
            second_user.save_user()

            found_user = User.find_user_by_password("k2r$678")
            self.assertEqual(found_user.password,second_user.password)


    def test_delete_user(self):
            """
            this method tests whether we can remove a user from our user list.
            """
            self.new_user.save_user()
            second_user = User("kayleen","green","k2r$678") # new user
            second_user.save_user()

            self.new_user.delete_user()
            self.assertEqual(len(User.user_list),2)

    def test_user_exists(self):
            """
            tests to check if we can return a boolean if we cannot find the user
            """
            self.new_user.save_user()
            second_user = User("kayleen","green","k2r$678") # new user
            second_user.save_user()


            user_exists = User.user_exists("k2r$678")
            self.assertTrue(user_exists)

    def test_display_all_users(self):
            """
            this method returns a list of all users saved
            """
            self.assertEqual(User.display_user(),User.user_list)



        
    if __name__ == '__main__':
        unittest.main()
