#!/usr/bin/python3
"""
module that define the BaseModel class which all classes will inherit from
"""
import uuid
from datetime import datetime, timezone, timedelta
import models


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
            models.storage.new(self)
        else:
            if 'id' not in kwargs:
                kwargs['id'] = str(uuid.uuid4())
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                if key == "updated_at":
                    self.updated_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                if key == "id":
                    self.id = value
                s1 = "updated_at"
                s2 = "created_at"
                if key != "__class__" and key != s1 and key != s2:
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
        models.storage.save()

    def to_dict(self):
        """returns the dict representation of the
        object
        """
        form = '%Y-%m-%dT%H:%M:%S.%f'
        dct = {**self.__dict__}
        dct["__class__"] = self.__class__.__name__
        if isinstance(self.created_at, datetime):
            dct["created_at"] = self.created_at.strftime(form)
        if isinstance(self.updated_at, datetime):
            dct["updated_at"] = self.updated_at.strftime(form)
        return dct

    @classmethod
    def all(cls):
        """class meth to retrieve all current instances of cls"""
        return models.storage.find_all(cls.__name__)

    @classmethod
    def count(cls):
        """method to get the number of all current instances of cls"""
        return len(models.storage.find_all(cls.__name__))

    @classmethod
    def create(cls, *args, **kwargs):
        """method to create an Instance"""
        new = cls(*args, **kwargs)
        return new.id

    @classmethod
    def show(cls, instance_id):
        """method to retrieve an instance"""
        return models.storage.find_by_id(
            cls.__name__,
            instance_id
        )

    @classmethod
    def destroy(cls, instance_id):
        """Deletes an instance"""
        return models.storage.delete_by_id(
            cls.__name__,
            instance_id
        )

    @classmethod
    def update(cls, instance_id, *args):
        """method to update an instance"""
        if not len(args):
            print("** attribute name missing **")
            return
        if len(args) == 1 and isinstance(args[0], dict):
            args = args[0].items()
        else:
            args = [args[:2]]
        for arg in args:
            models.storage.update_one(
                cls.__name__,
                instance_id,
                *arg
            )
