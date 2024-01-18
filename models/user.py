#!/usr/bin/python3

"""This file defines the UserModel class
It inherits from the BaseModel
"""


from models.base_model import BaseModel


class User(BaseModel):
    """The User Model"""

    # Attributes
    email = ""
    password = ""
    first_name = ""
    last_name = ""
