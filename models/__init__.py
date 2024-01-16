#!/usr/bin/python3

"""
Initializes  the module global (singleton) variables
"""

from .engine.file_storage import FileStorage
"""
Retrieves the storage instance
"""
storage = FileStorage()
storage.reload()
