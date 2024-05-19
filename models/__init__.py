#!/usr/bin/python3
""" FileStorage for managing object serialization and deserialization """
from models.engine.file_storage import FileStorage


# create the variable storage, an instance of FileStorage
storage = FileStorage()
# call reload() method on this variable
storage.reload()
