#!/usr/bin/python3
"""
Defines  the Amenity model
and inherits from BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity Mode"""

    # Attributes
    name: str = ''
