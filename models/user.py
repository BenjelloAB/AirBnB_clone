#!/usr/bin/python3
"""
This module inherits from BaseModel
and defines  UserModel class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from
    BaseModel"""
    email: str = ''
    password: str = ''
    first_name: str = ''
    last_name: str = ''
