#!/usr/bin/pytho3
"""
Defining FileStorage Class
"""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    Class for Serializes and Deserializes
    Class Attributes:
    __file_path - string with JSON file path ('file.json')
    """
    __file_path = "file.json"
    """path to the JSON file"""
    __objects = {}
    """is a dictionary"""

    def all(self):
        """returns the dict __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        """class name of an obj + id"""
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        newdict_objects = {}
        """new dict to store the keys and value that will save"""
        for key in self.__objects:
            """pass trought for each key/value"""
            newdict_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as json_f:
            """file handling"""
            json.dump(newdict_objects, json_f)
            """
            dumps: encode json data
            converts dict object into JSON string data format
            and write to file
            """

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            if os.path.isfile(self.__file_path):
                with open(self.__file_path, 'r') as json_f:
                    dict_objs = json.load(json_f)
                    """loads: decode json data"""
                for key, value in dict_objs.items():
                    self.__objects[key] = BaseModel(**val)
        except:
            pass
