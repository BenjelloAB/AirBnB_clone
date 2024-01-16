#!/usr/bin/python3
"""
Defines  the Error Messages in file storage
"""


class ModelNotFoundError(Exception):
    """will be raised when an unknown module is passed"""
    def __init__(self, arg="BaseModel"):
        super().__init__(f"Model with name {arg} is not registered!")


class InstanceNotFoundError(Exception):
    """will be raised when an unknown id  is passed"""

    def __init__(self, obj_id="", mod="BaseModel"):
        super().__init__(
                f"Insatnce of {mod} with id {obj_id} does not exist!")
