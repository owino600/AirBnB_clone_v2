#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, string
import os
from sqlalchemy.orm import relationship
from models.city import City
from models import type_storage

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if type_storage == 'db':
        cities = relationship("City", back_populates="state", cascade="all, delete")
    
