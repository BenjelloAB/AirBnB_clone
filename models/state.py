#!/usr/bin/python3
"""
This module defines a stateModel class
"""


from models.base_model import BaseModel


class State(BaseModel):
    """state model"""
    name: str = ''
