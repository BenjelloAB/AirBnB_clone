#!/usr/bin/python3
"""
Defines review model and inherits
from BaseModel
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Review class"""
    place_id: str = ''
    user_id: str = ''
    text: str = ''
