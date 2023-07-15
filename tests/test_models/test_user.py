#!/usr/bin/python3
"""
Defines unittests for models/user.py

"""
from models.user import User
from models import storage
from models.base_model import BaseModel
from datetime import datetime
import unittest
import time
import re
import json
import os
import uuid


class TestUser(unittest.TestCase):
    """
    unit test for user class

    """

    def test_instantiation(self):
        """
        Tests the instantiation of the User class.

        """

        q = User()
        self.assertEqual(str(type(q)), "<class 'models.user.User'>")
        self.assertIsInstance(q, User)
        self.assertTrue(issubclass(type(q), BaseModel))

    def test_uuids(self):
        """
        tests if two users have unique ids

        """
        us = User()
        us2 = User()
        self.assertNotEqual(us.id, us2.id)

    def test_attribute(self):
        """
        Tests the attributes

        """
        amen = User()
        self.assertEqual(str, type(User.email))
        self.assertIn("email", dir(User()))
        self.assertNotIn("email", amen.__dict__)

    def test_class(self):
        """
        Tests if the class is named correctly.

        """
        us = User()
        self.assertEqual(us.__class__.__name__, "User")

    def test_inherit(self):
        """
        Tests if class User inherits from BaseModel.

        """
        us = User()
        self.assertTrue(issubclass(us.__class__, BaseModel))




if __name__ == "__main__":
    unittest.main()
