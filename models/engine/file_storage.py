#!/usr/bin/python3
""" Defines a class FileStorage that handles serialization of instances to a JSON
file and deserialization of JSON file back to instances """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """ Manages storage of objects through serialization and deserialization. """
    
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects. """
        return FileStorage.__objects

    def new(self, obj):
        """ Adds the object to __objects with a key formatted as <obj class name>.id. """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file specified by __file_path. """
        objects_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(objects_dict, file)

    def reload(self):
        """ Deserializes the JSON file to __objects if the file exists, otherwise does nothing. """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                objects_dict = json.load(file)
                for key, obj_data in objects_dict.items():
                    class_name = key.split('.')[0]
                    cls = self._get_class_by_name(class_name)
                    if cls:
                        self.new(cls(**obj_data))
        except FileNotFoundError:
            pass

    def _get_class_by_name(self, class_name):
        """ Returns the class object based on class_name. """
        classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Place': Place,
            'Amenity': Amenity,
            'Review': Review
        }
        return classes.get(class_name)


