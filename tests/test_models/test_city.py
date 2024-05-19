#!/usr/bin/python3
"""Defines tests for the City class, defined in the city module"""
from models.city import City
from models.base_model import BaseModel
import unittest


class TestCity(unittest.TestCase):
    """Define City attributes and methods tests"""

    def setUp(self):
        """Instantiate City test objects"""
        self.city = City()

    def test_city_instantiation(self):
        """Test that City class correctly instantiates"""
        self.assertTrue(isinstance(self.city, City))

    def test_city_has_name_attribute(self):
        """Test that City class contains name public attribute"""
        self.assertTrue(hasattr(self.city, 'name'))

    def test_city_has_state_id_attribute(self):
        """Test that City class contains state_id public attribute"""
        self.assertTrue(hasattr(self.city, 'state_id'))

    def test_city_does_not_have_password_attribute(self):
        """Test that City class does not contain password public attribute"""
        self.assertFalse(hasattr(self.city, 'password'))

    def test_city_inherits_from_BaseModel(self):
        """Test that City class inherits from BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))
