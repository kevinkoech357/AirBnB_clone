#!/usr/bin/python3

"""
Creates a new instance of FileStorage
"""


# importing FileStorage module
from models.engine.file_storage import FileStorage


# creating storage, an instance of FileStorage
storage = FileStorage()
storage.reload()
