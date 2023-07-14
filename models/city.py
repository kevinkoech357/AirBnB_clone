#!/usr/bin/python3

"""
A module that creates child
class City
"""


# importing BaseModel
from models.base_model import BaseModel


class City(BaseModel):
    """
    A child class with state_id
    and name class attributes
    """
    state_id = ""
    name = ""
