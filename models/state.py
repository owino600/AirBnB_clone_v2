#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class State(BaseModel, Base):
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="state", cascade="all, delete")
    """ State class """
    name = ""
