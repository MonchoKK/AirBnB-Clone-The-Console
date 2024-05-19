#!/usr/bin/python3
"""Defines tests for the User class, defined in the user module"""
from models.user import User
from models.base_model import BaseModel
import unittest


class TestUser(unittest.TestCase):
    """Define User attributes and methods tests"""

    def setUp(self):
        """Instantiate User test objects"""
        self.user = User()

    def test_user_instantiation(self):
        """Test that User class correctly instantiates"""
        self.assertTrue(isinstance(self.user, User))

    def test_user_has_email_attribute(self):
        """Test that User class contains email public attribute"""
        self.assertTrue(hasattr(self.user, 'email'))

    def test_user_has_first_name_attribute(self):
        """Test that User class contains first_name public attribute"""
        self.assertTrue(hasattr(self.user, 'first_name'))

    def test_user_has_password_attribute(self):
        """Test that User class contains password public attribute"""
        self.assertTrue(hasattr(self.user, 'password'))

    def test_user_has_last_name_attribute(self):
        """Test that User class contains last_name public attribute"""
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_user_inherits_from_BaseModel(self):
        """Test that User class inherits from BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))
