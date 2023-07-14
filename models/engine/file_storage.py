#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""A module for file storage
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import path


class FileStorage:
    """Class for file storage
    Attributes:
        __file_path (str):JSON file path
        __objects (dict): stores all instances
    """
    __file_path = 'objects.json'
    __objects = {}

    def all(self):
        """Gets the __objects content
        Returns the content of the `__objects` class attribute.
        """
        return self.__objects

    def new(self, obj):
        """Saves a new object in the `__objects` attribute
        Args:
            obj (inst): Object that adds to  `__objects` class attribute
        Sets in the `__objects` class attribute the instance data
        with a key as <obj class name>.id.
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes the contents of `__objects`
        Contents of `__objects` class attribute  serialized
        to  `__file_path` class attribute in JSON format
        with the `created_at` and `updated_at` formatted.
        """
        json_dict = {}
        for k, v in self.__objects.items():
            json_dict[k] = v.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            f.write(json.dumps(json_dict))

    def reload(self):
        """Deserializes the JSON file in `__file_path` class attribute
        If the file on `__file_path` class attribute exists, each object
        on the file will be deserialized and appended to the `__objects`.
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                json_dict = json.loads(f.read())
                for k, v in json_dict.items():
                    self.__objects[k] = eval(v['__class__'])(**v)
