#!/usr/bin/python3

"""This file defines the review model
it inherits from the basemodel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """the review model"""

    # Attributes
    place_id = ""
    user_id = ""
    text = ""
