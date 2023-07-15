#!/usr/bin/python3

"""
A module that creates a child
class Amenity
"""


# importing BaseModel
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    A child class with name public
    class attribute
    """
    name = ""
