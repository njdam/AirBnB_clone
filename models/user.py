#!/usr/bin/python3
# A file with class User that inherits from BaseModel

from models.base_model import BaseModel


class User(BaseModel):
    """A class User that inherits from BaseModel."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *arg, **kwargs):
        """A function to initialise User instance."""
        super().__init__(*args, **kwargs)
