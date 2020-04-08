#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
import models
import os
from models.city import Cit
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
                """Property getter of list of city instances
                where state_id equals current State.id"""
                city_dict = models.storage.all(City)
                return [city for city in city_dict.values()
                        if city.state_id == self.id]
