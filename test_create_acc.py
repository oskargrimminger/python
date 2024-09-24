import hashlib
import unittest


def valid_login(username, password, users):
    salt = "5gz"
    dataBase_password = password + salt
    hashed_password = hashlib.md5(dataBase_password.encode()).hexdigest()

    if username in users and users[username] == hashed_password:
        return True 
    else:
        return False  


class TestLoginValidation(unittest.TestCase):
    
    def setUp(self):

        self.users = {}
        salt = "5gz"
        password = "testpass"
        hashed_password = hashlib.md5((password + salt).encode()).hexdigest()
        self.users['testuser'] = hashed_password

    def test_login_success(self):
        result = valid_login('testuser', 'testpass', self.users)
        self.assertTrue(result)


    def test_login_failure_wrong_password(self):
        result = valid_login('testuser', 'wrongpass', self.users)
        self.assertFalse(result)

    def test_login_failure_nonexistent_user(self):
        result = valid_login('nonexistent', 'testpass', self.users)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()

