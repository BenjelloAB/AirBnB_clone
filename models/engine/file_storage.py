#!/usr/bin/python3
"""module defining the file storage engine class"""
import json
from json.decoder import JSONDecodeError
from .errors import *
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    models = (
            "BaseModel",
            "User", "City", "State", "Place",
            "Amenity", "Review"
            )

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key_format = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key_format] = obj

    def save(self):
        ser = {}
        for key, value in FileStorage.__objects.items():
            ser[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(ser, f)

    def reload(self):
        try:
            des = {}
            with open(FileStorage.__file_path, "r") as f:
                des = json.loads(f.read())
            from models.base_model import BaseModel
            for key, dict_obj in des.items():
                st = dict_obj["__class__"]
                FileStorage.__objects[key] = eval(st)(**dict_obj)
                # FileStorage.__objects[key] = BaseModel(**dict_obj)
        except (FileNotFoundError, JSONDecodeError):
            pass

    def find_by_id(self, model, obj_id):
        """Find and return an elemt of model by its id"""
        F = FileStorage
        if model not in F.models:
            # Invalid Model Name
            # Not yet Implemented
            raise ModelNotFoundError(model)

        key = model + "." + obj_id
        if key not in F.__objects:
            # invalid id
            # Not yet Implemented
            raise InstanceNotFoundError(obj_id, model)

        return F.__objects[key]

    def delete_by_id(self, model, obj_id):
        """Find and return an elemt of model by its id"""
        F = FileStorage
        if model not in F.models:
            raise ModelNotFoundError(model)

        key = model + "." + obj_id
        if key not in F.__objects:
            raise InstanceNotFoundError(obj_id, model)

        del F.__objects[key]
        self.save()

    def find_all(self, model=""):
        """Find all instances or instances of model"""
        if model and model not in FileStorage.models:
            raise ModelNotFoundError(model)
        results = []
        for key, val in FileStorage.__objects.items():
            if key.startswith(model):
                results.append(str(val))
        return results

    def update_one(self, model, iid, field, value):
        """method to update an instance"""
        Fi = FileStorage
        if model not in Fi.models:
            raise ModelNotFoundError(model)

        key = model + "." + iid
        if key not in Fi.__objects:
            raise InstanceNotFoundError(iid, model)
        if field in ("id", "updated_at", "created_at"):
            return
        inst = Fi.__objects[key]
        try:
            vtype = type(inst.__dict__[field])
            inst.__dict__[field] = vtype(value)
        except KeyError:
            inst.__dict__[field] = value
        finally:
            inst.updated_at = datetime.utcnow()
            self.save()
