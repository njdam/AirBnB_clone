#!/usr/bin/python3
# A file that bear a class City inherited from class BaseModel.

from models.base_model import BaseModel


class City(BaseModel):
    """A class City that inherited from BaseModel.

       Attributes:
           state_id (str): is the id for state.
           name (str): is name of the city.
    """
    state_id = ""
    name = ""
