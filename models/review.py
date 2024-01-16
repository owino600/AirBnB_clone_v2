#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel):

    __tablename__ = "reviews"

    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), nullable=False, ForeignKey="places.id")
    user_id = Column(String(60), nullable=False, ForeignKey="users.id")
    """ Review classto store review information """
    place_id = ""
    user_id = ""
    text = ""
