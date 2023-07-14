#!/usr/bin/python3

"""
A module that serializes instances to
a JSON file and deserializes JSON
file to instances
"""


# importing libraries
import json


class FileStorage:
    """
    Definition of class FileStorage
    """
    # file path
    __file_path = "file.json"
    # create empty dict to store all objects
    __objects = {}

    def all(self):
        """
        Return dictionary objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj
        with key <obj class name>.id
        """
        key = "{} {}".format(obj__class__.name, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the
        JSON file (path: __file_path)
        """
        object_dict = {}
        for key, value in self.__object.items():
            object_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dumps(object_dict, file)

    def reload(self):
        """
        Deserialize the JSON file to objects
        """
