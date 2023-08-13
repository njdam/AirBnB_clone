#!/usr/bin/python3
# A file that bear class Amenity and inherited from class BaseModel.

from models.base_model import BaseModel


class Amenity(BaseModel):
    """A class Amenity that inherited from BaseModel class.
    A public class attribute:
        name: string - empty string.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialisation of class Amenity."""
        super().__init__(self, *args, **kwargs)