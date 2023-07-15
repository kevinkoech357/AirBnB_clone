#!/usr/bin/python3
"""
Defines unittests for models/place.py

"""
from models.place import Place
from models import storage
from models.base_model import BaseModel
from datetime import datetime
import unittest
import time
import re
import json
import os
import uuid


class TestPlace(unittest.TestCase):
    """
    unit test for the place class

    """

    def test_instantiation(self):
        """
        Tests the instantiation of Place class.

        """

        q = Place()
        self.assertEqual(str(type(q)), "<class 'models.place.Place'>")
        self.assertIsInstance(q, Place)
        self.assertTrue(issubclass(type(q), BaseModel))

    def test_uuids(self):
        """
        tests if two places have unique ids

        """
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

    def test_attribute(self):
        """
        Tests the attributes

        """
        p = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(Place()))
        self.assertNotIn("name", p.__dict__)

    def test_class(self):
        """
        Tests if the class Place is named correctly.

        """
        p = Place()
        self.assertEqual(p.__class__.__name__, "Place")

    def test_inherit(self):
        """
        Tests if class Place inherits from BaseModel.

        """
        p = Place()
        self.assertTrue(issubclass(p.__class__, BaseModel))


if __name__ == "__main__":
    unittest.main()
