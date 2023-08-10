#!/usr/bin/python3
# A file which bears a BaseModel class

import models
import uuid
from datetime import datetime


class BaseModel:
    """
    A class BaseModel where all model's classes inherited.
    """

    def __init__(self, *arg, **kwargs):
        """
        Initiatisation of every BaseModal with it's unique Id.

        Args:
            *args (any): Unused.
            **kwargs (dict): are pairs of attributes of Key/Value
        """
        t_format = '%Y-%m-%dT%H:%M:%S.%f'
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, t_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """
        A function to save a public attribute `updated_at` with current time
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        A function to return a Dictionary represenation of a class.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['__class__'] = self.__class__.__name__

        return (obj_dict)

    def __str__(self):
        """
        A function to return a String represantion of a class.
        """
        class_name = self.__class__.__name__

        return ("[{}] ({}) ({})".format(class_name, self.id, self.__dict__))
