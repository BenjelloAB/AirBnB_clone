#!/usr/bin/python3
"""module defining the file storage engine class"""
import json
from json.decoder import JSONDecodeError


class FileStorage:
    __file_path = "file.json"
    __objects = {}

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
                st = dict_obj["__class_"]
                FileStorage.__objects[key] = eval(st)(**dict_obj)
                # FileStorage.__objects[key] = BaseModel(**dict_obj)
        except (FileNotFoundError, JSONDecodeError):
            pass
