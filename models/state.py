#!/usr/bin/python3

"""This file defines the state model
it inherits from the basemodel
"""


from models.base_model import BaseModel


class State(BaseModel):
    """The state model"""

    #Attribute
    name: str = ""