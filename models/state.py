#!/usr/bin/python3

"""This file defines the State Model
It inherits from the BaseModel
"""


from models.base_model import BaseModel


class State(BaseModel):
    """The State Model"""

    # Attributes
    name: str = ""
