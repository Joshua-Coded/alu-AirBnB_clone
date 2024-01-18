#!/usr/bin/python3

"""This file defines the Review Model
It inherits from the BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """The Review Model"""

    # Attributes
    place_id: str = ""
    user_id: str = ""
    text: str = ""
