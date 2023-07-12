#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This module creates a parent
class BaseModel.
"""


# importing libraries
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Parent class.
    """
    def __init__(self):
        """
        Instantiation method with
        id,created_at and updated
        at instance attributes.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        String representation of BaseModel
        """
        # Gets name of class that self is an instance of
        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))
