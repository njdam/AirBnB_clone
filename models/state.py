#!/usr/bin/python3
# A file that bear class State and inherited from class BaseModel.

from models.base_model import BaseModel


class State(BaseModel):
    """A class State that inherited from BaseModel class.
    A public class attribute:
        name: string - empty string.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialisation of class State."""
        super().__init__(self, *args, **kwargs)
