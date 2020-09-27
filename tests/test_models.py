import unittest
from app.models import User, Blog, Comment

class TestUser(unittest.TestCase):
    '''class to test behaviour of User Model'''
    def setUp(self):
        self.new_user = User(password = 'Abdi9999')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_accessing_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('Abdi999'))