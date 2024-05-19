#!/usr/bin/python3
"""
    Defines the BaseModel class that serves as a foundation for all other classes
    in the project, providing common attributes and methods.
"""
import uuid
from datetime import datetime


class BaseModel:
    """ A base class that provides common attributes and methods for other classes. """
    
    def __init__(self, *args, **kwargs):
        """ Initializes an instance with attributes based on provided keyword arguments
        or assigns default values if no keyword arguments are given.
        """
        if kwargs:
            self._init_from_kwargs(kwargs)
        else:
            self._init_new_instance()

    def _init_from_kwargs(self, kwargs):
        """ Initializes instance attributes from a dictionary representation. """
        for key, value in kwargs.items():
            if key in ('created_at', 'updated_at'):
                setattr(self, key, datetime.fromisoformat(value))
            elif key == '__class__':
                continue
            else:
                setattr(self, key, value)

    def _init_new_instance(self):
        """ Initializes a new instance with default values. """
        from models import storage
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        storage.new(self)

    def __str__(self):
        """ Returns a string representation of the instance. """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Updates the updated_at attribute with the current datetime and saves the instance. """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary representation of the instance, including a __class__ key. """
        instance_dict = {key: (value.isoformat() if isinstance(value, datetime) else value)
                         for key, value in self.__dict__.items()}
        instance_dict['__class__'] = self.__class__.__name__
        return instance_dict


