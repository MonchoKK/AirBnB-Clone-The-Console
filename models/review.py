#!/usr/bin/python3
""" Defines the class Review, that inherits from class BaseModel """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Defines the attributes/methods of a Review instance """

    # Define (public) class attributes
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """ Initializes Review objects """
        # Initialize superclass
        super().__init__(*args, **kwargs)
