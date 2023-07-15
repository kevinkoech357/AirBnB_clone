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


class Test_City(unittest.TestCase):
    """
    unit test for the city class

    """

    def test_instantiation(self):
        """
        Tests the instantiation of the City class.
        
        """

        q = City()
        self.assertEqual(str(type(q)), "<class 'models.city.City'>")
        self.assertIsInstance(q, City)
        self.assertTrue(issubclass(type(q), BaseModel))

    def test_uuids(self):
        """
        tests if two cities have unique ids

        """
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_attribute(self):
        """
        Tests the attributes

        """
        c = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(City()))
        self.assertNotIn("name", c.__dict__)

    def test_class(self):
        """
        Tests if the class is named correctly.

        """
        c = City()
        self.assertEqual(c.__class__.__name__, "City")

    def test_inherit(self):
        """
        Tests if class City inherits from BaseModel.

        """
        c = City()
        self.assertTrue(issubclass(c.__class__, BaseModel))




if __name__ == "__main__":
    unittest.main()
