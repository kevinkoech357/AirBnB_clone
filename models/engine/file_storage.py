#!/usr/bin/python3

"""
A module that serializes instances to
a JSON file and deserializes JSON
file to instances
"""


# importing libraries and modules
import json
# import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

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
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the
        JSON file (path: __file_path)
        """
        object_dict = {}
        for key, value in self.__objects.items():
            object_dict[key] = value.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(object_dict, file)

    def reload(self):
        """
        Deserialize the JSON file to objects
        """
        class_dict = {
            'BaseModel' : BaseModel,
            'Amenity' : Amenity,
            'City': City,
            'Place': Place,
            'Review': Review,
            'State': State,
            'User': User
        }

        # if os.path.isfile(self.__file_path):
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                # read file contents
                # file_content = file.read()
                # deserialize the json string
                object_dict = json.load(file)
                # print(object_dict)
                for key, value in object_dict.items():
                    class_name, object_id = key.split(".")
                    # class_object = eval(class_name) - security risk
                    self.__objects[key] = globals()[class_name](**value)
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    storage = FileStorage()
    storage.reload()
