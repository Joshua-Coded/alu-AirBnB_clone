#!/usr/bin/python3

"""This file defines the City Model
It inherits from the BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """The City Model"""

    # Attributes
    name: str = ""
    state_id: str = ""
