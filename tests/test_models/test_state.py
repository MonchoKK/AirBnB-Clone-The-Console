#!/usr/bin/python3
"""Defines tests for the State class, defined in the state module"""
from models.state import State
from models.base_model import BaseModel
import unittest


class TestState(unittest.TestCase):
    """Define State attributes and methods tests"""

    def setUp(self):
        """Instantiate State test objects"""
        self.state = State()

    def test_state_instantiation(self):
        """Test that State class correctly instantiates"""
        self.assertIsInstance(self.state, State)

    def test_state_has_name_attribute(self):
        """Test that State class contains name public attribute"""
        self.assertTrue(hasattr(self.state, 'name'))

    def test_state_name_is_str(self):
        """Test that name public attribute is a string"""
        self.assertIsInstance(getattr(self.state, 'name', None), str)

    def test_state_nonExistent_attribute_does_not_exist(self):
        """Test that State class does not contain public attribute, nonExistent"""
        self.assertIsNone(getattr(self.state, 'nonExistent', None))

    def test_state_inherits_from_BaseModel(self):
        """Test that State class inherits from BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))
