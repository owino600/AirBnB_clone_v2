#!/usr/bin/python3
""" State Module for HBNB project """
from aqlalchemy.ext.declarative import declarative_base
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
    
    else:
        def cities(all):
            var = models.storage.all()
            listu = []
            result = []
            
            for key in var:
                cities = key.replace('.', ' ')
                cities = shlex.split(reviews)
                if (cities[0] == 'City'):
                    listu .append(var[key])
            for val in listu:
                if (val.state_id == self.id):
                    result.append(val)
            return (result) 