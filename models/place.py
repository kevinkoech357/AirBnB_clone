#!/usr/bin/python3

"""
A module that creates child
class Place
"""


# importing BaseModel
from models.base_model import BaseModel


class Place(BaseModel):
    """
    A child class that has a couple
    of attributes
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitute = 0.0
    longitude = 0.0
    amenity_ids = []
