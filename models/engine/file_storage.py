#!/usr/bin/python3

"""
A module that serializes instances to
a JSON file and deserializes JSON
file to instances
"""


# importing libraries and modules
import json
from models.base_model import BaseModel


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
        key = "{} {}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the
        JSON file (path: __file_path)
        """
        object_dict = {}
        for key, value in self.__objects.items():
            object_dict[key] = value.to_dict()

        with open(self.__file_path, "w") as file:
            json.dumps(object_dict, file)

    def reload(self):
        """
        Deserialize the JSON file to objects
        """
        try:
            with open(self.__file_path, "r") as file:
                # read file contents
                file_content = file.read()
                # deserialize the json string
                object_dict = json.load(file_content)
                # print(object_dict)
                self.__objects = {}
                for key, value in object_dict.items():
                    class_name, object_dict = key.split(".")
                    # class_object = eval(class_name) - security risk
                    self.__objects[key] = eval(value["__class__"])(**value)
        except FileNotFoundError:  # if file is not found
            pass

if __name__ == "__main__":
    storage = FileStorage()
    storage.reload()
