import unittest
from create_account.py import register, login, users  

class TestUserManagement(unittest.TestCase):

    def setUp(self):
        users.clear()

    def test_register(self):
        result = register("user1", "pass1")
        self.assertIn("Registered successfully", result)
        self.assertIn("user1", users)

    def test_login_success(self):
        register("user1", "pass1")
        result = login("user1", "pass1")
        self.assertEqual(result, "Welcome, user1!")

    def test_login_invalid_username(self):
            register("user1", "pass1")
            result = login("invaliduser", "pass1")
            self.assertEqual(result, "Password or Username is incorrect")

    def test_login_invalid_password(self):
        register("user1", "pass1")
        result = login("user1", "wrongpassword")
        self.assertEqual(result, "Password or Username is incorrect")

if __name__ == "__main__":
    unittest.main()






