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
    """
    Tests for BaseModel
    """
    def setUp(self):
        self.base_model = BaseModel()

    def test_init_method(self):
        """
        Test init method
        """
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str(self):
        """
        Test str method
        """
        output = ("[BaseModel] ({}) {}".format(
            self.base_model.id, self.base_model.__dict__))
        self.assertEqual(str(self.base_model), output)
        test1 = BaseModel()
        test2 = BaseModel()
        self.assertNotEqual(test1.__str__(), test2.__str__())

    def test_save(self):
        """
        Test save method
        """
        prev_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(prev_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        """
        Test for to_dict method
        """
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertTrue(isinstance(bm_dict, dict))
        self.assertTrue("__class__" in bm_dict)

    def test_unique_ids(self):
        """
        Test unique ids
        """
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_id_type(self):
        """
        Test if id is str
        """
        bm = BaseModel()
        self.assertEqual(str, type(bm.id))
