#!/usr/bin/python3

"""
A module that creates child
class review
"""


# importing BaseModel
from models.base_model import BaseModel


class Revie(BaseModel):
    """
    A class that inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
