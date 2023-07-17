#!/usr/bin/python3
"""
Defines unittests for models/amenity.py

"""
import models
from models import *
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
    unit test for amenity class which
    includes various methods of different tests

    """
    def setUp(self):
        """
        Create new environment before each test
        """
        self.amenity = Amenity()

    def tearDown(self):
        """
        Clean up environment after test
        """
        pass

    def test_instantiation(self):
        """
        Tests the instantiation of Amenity class.
        """
        q = Amenity()
        self.assertEqual(str(type(q)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(q, Amenity)
        self.assertTrue(issubclass(type(q), BaseModel))

    def test_init_with_args(self):
        """
        Test init with args
        """
        input_data = {
            'id': '123',
            'created_at': '2023-07-07T00:00:00',
            'updated_at': '2023-07-07T00:00:00',
            'name': 'Test'
            }

        amenity = Amenity(**input_data)

        # verify if attributes are set correctly
        self.assertEqual(amenity.id, '123')
        self.assertEqual(amenity.created_at,
                         datetime.fromisoformat('2023-07-07T00:00:00'))
        self.assertEqual(amenity.updated_at,
                         datetime.fromisoformat('2023-07-07T00:00:00'))
        self.assertEqual(amenity.name, 'Test')

    def test_init_without_args(self):
        """
        Test init without args
        """
        amenity = Amenity()

        self.assertIsNotNone(amenity.id)
        self.assertIsNotNone(amenity.created_at)
        self.assertIsNotNone(amenity.updated_at)
        self.assertEqual(amenity.created_at, amenity.updated_at)

    def test_args(self):
        """
        Testing *args
        """
        amenity = Amenity(None)
        self.assertNotIn(None, amenity.__dict__.values())

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
