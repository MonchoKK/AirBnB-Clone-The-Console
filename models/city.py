#!/usr/bin/python3
""" Defines the class City, that inherits from class BaseModel """
from models.base_model import BaseModel


class City(BaseModel):
    """ Defines the attributes/methods of a City instance """
    
    # Define (public) class attributes
    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        """ Initializes City objects """
        # Initialize superclass
        super().__init__(*args, **kwargs)
