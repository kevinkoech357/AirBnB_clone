#!/usr/bin/python3
"""
Defines unittests for models/review.py

"""
from models.review import Review
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime
import unittest
import time
import re
import json
import os
import uuid


class TestReview(unittest.TestCase):
    """
    unit test for the Review class

    """

    def test_instantiation(self):
        """
        Tests the instantiation of the Review class.
        """

        q = Review()
        self.assertEqual(str(type(q)), "<class 'models.review.Review'>")
        self.assertIsInstance(q, Review)
        self.assertTrue(issubclass(type(q), BaseModel))

    def test_uuids(self):
        """
        tests to check unique ids

        """
        r = Amenity()
        r2 = Amenity()
        self.assertNotEqual(r.id, r2.id)

    def test_attribute(self):
        """
        Tests the attributes

        """
        amen = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(Review()))
        self.assertNotIn("place_id", amen.__dict__)

    def test_class(self):
        """
        Tests if the class is named correctly.

        """
        r = Review()
        self.assertEqual(r.__class__.__name__, "Review")

    def test_inherit(self):
        """
        Tests if class Review inherits from BaseModel.

        """
        rev = Review()
        self.assertTrue(issubclass(rev.__class__, BaseModel))




if __name__ == "__main__":
    unittest.main()
