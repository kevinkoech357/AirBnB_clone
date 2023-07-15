#!/usr/bin/python3
"""
Defines unittests for file storage

"""
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
from models.user import User
from datetime import datetime
import unittest
import time
import re
import json
import os
import uuid


class TestFileStorage(unittest.TestCase):
    """
    unit test for FileStorage class

    """

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.user = User()
        cls.user.first_name = "Kevin"
        cls.user.last_name = "Mike"
        cls.user.email = "mk@gmail.com"
        cls.storage = FileStorage()
        cls.path = "file.json"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.user
        """ if delete the file """
        if os.path.exists("file.json"):
            os.remove("file.json")


    def test_docs(self):
        """Test docstrings"""
        self.assertIsNotNone(FileStorage.all)
        self.assertIsNotNone(FileStorage.new)
        self.assertIsNotNone(FileStorage.save)
        self.assertIsNotNone(FileStorage.reload)

    def test_all(self):
        """tests if all works in File Storage"""
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_new(self):
        """test when a new user is created"""
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.id = "123455"
        user.name = "Kevin"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])



if __name__ == "__main__":
    unittest.main()
