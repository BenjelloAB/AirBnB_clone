#!/usr/bin/python3
""" 
module that define the BaseModel class which all classes will inherit from
"""
import uuid
from datetime import datetime, timezone, timedelta
from models import storage


class BaseModel:
    """
    the base model class
    """
    
    def __init__(self, *args, **kwargs):
        """Init the object"""
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            if 'id' not in kwargs:
                kwargs['id'] = str(uuid.uuid4())
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "updated_at":
                    self.updated_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "id":
                    self.id = value
                elif key != "__class__" and key != "updated_at" and key != "created_at":
                    setattr(self, key, value)
                
                
    def __str__(self):
        """str representation of the current object"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)
    def save(self):
        """saves the object to the json file
        """
        self.updated_at = datetime.now()
        storage.save()
    
    def to_dict(self):
        """returns the dict representation of the 
        object
        """
        dct = self.__dict__
        dct["__class__"] = self.__class__.__name__
        dct["created_at"] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        dct["updated_at"] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return dct
