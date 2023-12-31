#!/usr/bin/python3
# A file to bear a class FileStorage to serialize instances to a JSON file
# and deserializes JSON file to instances

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """A class FileStorage that serializes instances to a JSON file and
       deserializes JSON file to instances.

       Attributes:
       __file_path (str): is the file name of a file where to save objects
       __objects (dict): is a dictionary of instantiated objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """A function to return dictionary __objects."""
        return (FileStorage.__objects)

    def new(self, obj):
        """Function to set in __objects obj with key <obj_class_name>.id"""
        # For getting the class name of the object or type(obj).__name__
        class_name = obj.__class__.__name__
        # This is creation of key for the object in the __objects dictionary
        key = "{}.{}".format(class_name, obj.id)
        # Adding the object to the __objects dictionary with the key
        FileStorage.__objects[key] = obj

    def save(self):
        """To serialize __objects to the JSON file __file_path."""
        # Getting Dictionary object
        dict_obj = FileStorage.__objects
        # Creation of a new dictionary with object IDs as keys and
        # their serialized representations as values
        new_dict = {obj: dict_obj[obj].to_dict() for obj in dict_obj.keys()}
        # The openning of the JSON file in written mode
        with open(FileStorage.__file_path, mode="w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """To deserialize JSON file __file_path to __objects, if it exist
        Otherwise, do nothing.
        """
        try:
            with open(FileStorage.__file_path) as f:
                # This load JSON data from file
                ldd_obj = json.load(f)

                # This iterate over the values in the loaded dictionary
                for ob in ldd_obj.values():
                    # This retrieve a class name from '__class__' key
                    cls_name = ob["__class__"]
                    # Removing '__class__' key from dictionary
                    del ob["__class__"]
                    # This create a new instance of class using eval()
                    # & pass remaining dictionary as keward arguments
                    self.new(eval(cls_name)(**ob))

        except FileNotFoundError:
            return
