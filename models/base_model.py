#!/usr/bin/python3

"""
This module creates a parent
class BaseModel.
"""


# importing libraries
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """
    Parent class.
    """
    def __init__(self, *args, **kwargs):
        """
        Instantiation method with
        id,created_at and updated
        at instance attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """
        String representation of BaseModel
        """
        # Gets name of class that self is an instance of
        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))

    def save(self):
        """
        Updates updated_at instance
        with the current time
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Creates a dictionary with all instance
        attributes and adds '__class__' key.
        Created_at and updated_at are
        converted to string format using
        isoformat() of datetime object
        """
        object_dict = self.__dict__.copy()
        object_dict["__class__"] = self.__class__.__name__
        object_dict["created_at"] = self.created_at.isoformat()
        object_dict["updated_at"] = self.updated_at.isoformat()
        return (object_dict)
