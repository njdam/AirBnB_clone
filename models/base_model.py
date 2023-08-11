#!/usr/bin/python3
# A file which bears a BaseModel class

import uuid
from datetime import datetime
from collections import OrderedDict


class BaseModel:
    """
    A class BaseModel where all model's classes inherited.
    """

    def __init__(self):
        """
        Initiatisation of every BaseModal with it's unique Id.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        A function to return a String represantion of a class.
        """
        str_rep = "[{}] ({})".format(self.__class__.__name__, self.id)
        str_rep += " {}".format(self.__dict__)

        return (str_rep)

    def save(self):
        """
        A function to save a public attribute `updated_at` with current time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        A function to return a Dictionary represenation of a class.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return (obj_dict)
