#!/usr/bin/python3

""" This file defines the UserModel class
It inherits from the BaseMode
"""


from models.base_model import BaseModel


class User(BaseModel):
    """ The user model"""

    #Attributes
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
