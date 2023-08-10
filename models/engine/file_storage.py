#!/usr/bin/python3
# A file to bear a class FileStorage to serialize instances to a JSON file
# and deserializes JSON file to instances

import json
from models.base_model import BaseModel


class FileStorage:
    """
    A class FileStorage that serializes instances to a JSON file and
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
        # For getting the class name of the object
        class_name = obj.__class__.__name__
        # This is creation of key for the object in the __objects dictionary
        key = "{}.{}".format(class_name, obj.id)
        # Adding the object to the __objects dictionary with the key
        FileStorage.__objects[key] = obj

    def save(self):
        """To serialize __objects to the JSON file __file_path."""
        # For getting dictionary objects
        dict_obj = FileStorage.__objects
        # Creation of a new dictionary with object IDs as keys and
        # their serialized representations as values
        dictobj = {obj: dict_obj[obj].to_dict() for obj in dict_obj.keys()}
        # The openning of the JSON file in written mode
        with open(FileStorage.__file_path, "w") as f:
            json.dump(dictobj, f)

    def reload(self):
        """To deserialize JSON file __file_path to __objects, if it exist"""
        try:
            with open(FileStorage.__file_path) as f:
                # This load JSON data from file
                dictobj = json.load(f)
                # This iterate over the values in the loaded dictionary
                for o in dictobj.values():
                    # This retrieve a class name from '__class__' key
                    class_name = o["__class__"]
                    # This remove the '__class__' key from the dictionary
                    del o["__class__"]
                    # This create a new instance of class using eval() and
                    # pass the remaining dictionary as keward arguments
                    self.new(eval(class_name)(**o))

        except FileNotFoundError:
            # This raise Error if file is not find.
            raise FileNotFoundError("File not found: {}".format(FileStorage.__file_path))
