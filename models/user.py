#!/usr/bin/python3
"""User class that inherits from BaseModel"""
from models.base_model import BaseModel

class User(BaseModel):
    """Represents a user with specific attributes"""

    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """Initialize a new User instance"""
        super().__init__(*args, **kwargs)  # Call the superclass's initializer
