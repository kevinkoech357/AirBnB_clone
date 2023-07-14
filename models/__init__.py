"""Initializes a variable `storage` to create a
unique `FileStorage` instance for the HBNB application.

"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
