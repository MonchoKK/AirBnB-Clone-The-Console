#!/usr/bin/python3
""" Defines the class State, that inherits from class BaseModel """
from models.base_model import BaseModel


class State(BaseModel):
    """ Defines the attributes/methods of a State instance """
    
    # Define (public) class attributes
    name = ''

    def __init__(self, *args, **kwargs):
        """ Initializes State objects """
        # Initialize superclass
        super().__init__(*args, **kwargs)
