#!/usr/bin/python3
"""
Defines uittests for models/city.py

"""
from models.city import City
from models import storage
from models.base_model import BaseModel
from datetime import datetime
import unittest
import time
import re
import json
import os
import uuid

#!/usr/bin/python3
"""Test Console"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import unittest


class TestConsole(unittest.TestCase):
    """
    unittest for the console
    """
    def test_class(self):
        """
        Unittest to check if all required classes
        are present
        """
        city1 = City()
        amenity1 = Amenity()
        state1 = State()
        rev1 = Review()
        place1 = Place()
        self.assertEqual(city1.__class__.__name__, "City")
        self.assertEqual(amenity1.__class__.__name__, "Amenity")
        self.assertEqual(state1.__class__.__name__, "State")
        self.assertEqual(rev1.__class__.__name__, "Review")
        self.assertEqual(place1.__class__.__name__, "Place")

    def test_inherit(self):
        """
        inherit correcly from BaseModel
        """
        city1 = City()
        amenity1 = Amenity()
        state1 = State()
        rev1 = Review()
        place1 = Place()
        self.assertTrue(issubclass(city1.__class__, BaseModel))
        self.assertTrue(issubclass(amenity1.__class__, BaseModel))
        self.assertTrue(issubclass(state1.__class__, BaseModel))
        self.assertTrue(issubclass(rev1.__class__, BaseModel))
        self.assertTrue(issubclass(place1.__class__, BaseModel))

