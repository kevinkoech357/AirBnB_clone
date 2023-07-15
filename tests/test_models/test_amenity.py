#!/usr/bin/python3
"""
Defines unittests for models/amenity.py

"""
from models.amenity import Amenity
from models import storage
from models.base_model import BaseModel
from datetime import datetime
import unittest
import time
import re
import json
import os
import uuid


class TestAmenity(unittest.TestCase):
    """
    unit test for amenity class

    """
    def test_instantiation(self):
        """
        Tests the instantiation of Amenity class.
        """
        q = Amenity()
        self.assertEqual(str(type(q)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(q, Amenity)
        self.assertTrue(issubclass(type(q), BaseModel))

    def test_uuids(self):
        """
        tests if two amenities have unique ids

        """
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_attribute(self):
        """
        Tests the attributes

        """
        amen = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", amen.__dict__)

    def test_class(self):
        """
        Tests if the class is named correctly.

        """
        amenity1 = Amenity()
        self.assertEqual(amenity1.__class__.__name__, "Amenity")

    def test_inherit(self):
        """
        Tests if class Amenity inherits from BaseModel.

        """
        amenity1 = Amenity()
        self.assertTrue(issubclass(amenity1.__class__, BaseModel))


if __name__ == "__main__":
    unittest.main()
