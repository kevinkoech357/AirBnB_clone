#!/usr/bin/python3
"""
Defines uittests for models/state.py

"""
from models.state import State
from models import storage
from models.base_model import BaseModel
from datetime import datetime
import unittest
import time
import re
import json
import os
import uuid


class TestState(unittest.TestCase):
    """
    unit test for State class

    """

    def test_instantiation(self):
        """
        Tests the instantiation of State class.

        """

        q = State()
        self.assertEqual(str(type(q)), "<class 'models.state.State'>")
        self.assertIsInstance(q, State)
        self.assertTrue(issubclass(type(q), BaseModel))

    def test_uuids(self):
        """
        tests if they all have unique ids

        """
        st = State()
        st2 = State()
        self.assertNotEqual(st.id, st2.id)

    def test_attribute(self):
        """
        Tests the attributes

        """
        st = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(State()))
        self.assertNotIn("name", st.__dict__)

    def test_class(self):
        """
        Tests if the class is named correctly.

        """
        st = State()
        self.assertEqual(st.__class__.__name__, "State")

    def test_inherit(self):
        """
        Tests if class State inherits from BaseModel.

        """
        st = State()
        self.assertTrue(issubclass(st.__class__, BaseModel))




if __name__ == "__main__":
    unittest.main()
