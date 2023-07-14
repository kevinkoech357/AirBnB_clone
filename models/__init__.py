<<<<<<< HEAD
"""Initializes a variable `storage` to create a
unique `FileStorage` instance for the HBNB application.

"""

from models.engine.file_storage import FileStorage

=======
#!/usr/bin/python3

"""
Creates a new instance of FileStorage
"""


# importing FileStorage module
from models.engine.file_storage import FileStorage


# creating storage, an instance of FileStorage
>>>>>>> 2a3efbff0bc123af7195fb69d07a0f1c2c09dd65
storage = FileStorage()
storage.reload()
