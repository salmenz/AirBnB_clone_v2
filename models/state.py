#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
import models
from models import storage


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="save-update, delete", backref="state")

    @property
    def cities(self):
        """ Getter attribut"""
        cities = storage.all(City)
        d = dict()
        for key, value in cities:
            if value.id == self.id:
                d[key] = value
        return (d)
