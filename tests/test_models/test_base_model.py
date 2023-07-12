#!/usr/bin/python3

"""
Unittests for BaseModel class
"""

# importing libraries
from datetime import datetime
from models.base_model import BaseModel
import unittest
from uuid import uuid4


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_init(self):
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str(self):
        output = ("[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__))
        self.assertEqual(str(self.base_model), output)
