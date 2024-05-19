#!/usr/bin/python3
""" Defines a class FileStorage that serializes instances to a JSON
file and deserializes JSON file to instances """
import json


class FileStorage:
    """ Defines attributes and methods that serializes instances
    to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {} # a dictionary of objects(<classname>.id: dict?)


    # define public instance methods
    def all(self):
        """ returns the dictionary __objects """
        pass

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        pass

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        pass

    def reload(self):
        """ deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        """
        pass
