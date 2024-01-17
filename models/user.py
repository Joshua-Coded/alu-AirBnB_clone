#!/usr/bin/python3

""" This file defines the UserModel class
It inherits from the BaseMode
"""


from models.base_model import BaseModel


class User(BaseModel):
    """ The user model"""

    # Attributes
    email = ""
    password = ""
    first_name = ""
    last_name = ""
