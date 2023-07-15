#!/usr/bin/python3

"""
A module that creates a child class
User that inherits from BaseModel
"""


# importing BaseModel module
from models.base_model import BaseModel


class User(BaseModel):
    """
    A child class with email,
    password, first_name and
    last_name public attributes
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
