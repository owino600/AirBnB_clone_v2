#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Table
import os
import models
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import type_storage

if type_storage == "db":
    place_amenity = Table("place_amenity", Base.metadata, Column('place_id', String(60), ForeignKey('place.id'), primary_key=True), Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))

    
class Place(BaseModel, Base):

    __tablename__ = 'places'

    """ A place to stay """
    city_id = Column(String(60), nullable=False, ForeignKey=("cities.id"))
    user_id = Column(String(60), nullable=False, ForeignKey=("users.id"))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    if type_storage == "db":
        reviews = relationship("Review", backref="place", cascade="all, delete")
        amenities = relationship("Amenity", secondary=place_amenity, back_populates='place_amenities')

    else:
        @property
        def reviews(self):
            var = models.storage.all()
            listu = []
            result = []
            for key in var:
                reviews = key.replace('.', ' ')
                reviews = shlex.split(reviews)
                if (reviews[0] == 'Review'):
                    listu .append(var[key])