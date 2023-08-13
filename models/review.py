#!/usr/bin/python3
# A file that bear class Review and inherited from class BaseModel.

from models.base_model import BaseModel


class Review(BaseModel):
    """A class State that inherited from BaseModel class.
    A public class attribute:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialisation of class Review."""
        super().__init__(self, *args, **kwargs)
