#!/usr/bin/python3
"""Defines tests for the User class."""
from models.user import User
from models.base_model import BaseModel
import unittest

class TestUser(unittest.TestCase):
    """Defines User attributes and methods tests."""
    
    def setUp(self):
        """Instantiate User test objects."""
        self.user = User()

    def test_user_instantiation(self):
        """Test that User class correctly instantiates."""
        self.assertIsInstance(self.user, User)

    def test_user_email_attribute(self):
        """Test that User class contains email public attribute and it's a string."""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertIsInstance(self.user.email, str)

    def test_user_first_name_attribute(self):
        """Test that User class contains first_name public attribute and it's a string."""
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertIsInstance(self.user.first_name, str)

    def test_user_password_attribute(self):
        """Test that User class contains password public attribute and it's a string."""
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertIsInstance(self.user.password, str)

    def test_user_last_name_attribute(self):
        """Test that User class contains last_name public attribute and it's a string."""
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertIsInstance(self.user.last_name, str)

    def test_user_is_instance_of_BaseModel(self):
        """Test that User class inherits from BaseModel."""
        self.assertIsInstance(self.user, BaseModel)
