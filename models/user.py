#!/usr/bin/python3
<<<<<<< HEAD
"""This module defines a class User"""
=======
"""Defines the User class."""
>>>>>>> refs/remotes/origin/main
from models.base_model import BaseModel


class User(BaseModel):
<<<<<<< HEAD
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
=======
    """Represent a User.
    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
>>>>>>> refs/remotes/origin/main
