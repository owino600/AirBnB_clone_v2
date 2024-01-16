#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import relationship


class City(BaseModel):
    places = relationship("Place", backref="cities",cascade="all, delete")
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""
