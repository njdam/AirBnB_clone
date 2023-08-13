#!/usr/bin/python3
# A file that bear a class City inherited from class BaseModel.

from models.base_model import BaseModel


class City(BaseModel):
    """A class City that inherited from BaseModel."""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialisation of class City."""
        super().__init__(*args, **kwargs)
