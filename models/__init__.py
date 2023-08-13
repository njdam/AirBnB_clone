#!/usr/bin/python3
# The __init__ magic method for models dictionary to get storage path

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
