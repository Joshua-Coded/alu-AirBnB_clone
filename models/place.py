#!/usr/bin/python3

"""This file defines the Place Model
It inherits from the BaseModel
"""

from models.base_model import BaseModel
from typing import List


class Place(BaseModel):
    """The Place Model"""

    # Attributes
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
