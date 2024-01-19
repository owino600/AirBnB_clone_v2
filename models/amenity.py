#!/usr/bin/python
""" holds class Amenity"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
<<<<<<< HEAD
from models import type_storage
from models.place import place_amenity
=======
from sqlalchemy.orm import relationship
>>>>>>> ae8a35f08e3067ef6f721081a0e8c49f198c4c7f


class Amenity(BaseModel, Base):
    """Representation of Amenity """
    if models.storage_t == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

<<<<<<< HEAD
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
=======
    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
>>>>>>> ae8a35f08e3067ef6f721081a0e8c49f198c4c7f
