#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    name = ""
