#!/usr/bin/python3
"""A file with class User that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """A class User that inherits from BaseModel.

    Atrributes:
        email (str): is the email of the user.
        password (str): is the password of the user.
        first_name (str): is the first name of the user.
        last_name (str): is the last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
