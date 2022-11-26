#!/usr/bin/python3
"""
creating a unique filestorage instance 
models module documentation
storage is a singleton to FileStorage
and reload objects to file.json
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
