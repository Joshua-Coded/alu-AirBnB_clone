#!/usr/bin/python3

"""This file defines the Amenity Model
It inherits from the BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """The Amenity Model"""

    # Attributes
    name: str = ""
