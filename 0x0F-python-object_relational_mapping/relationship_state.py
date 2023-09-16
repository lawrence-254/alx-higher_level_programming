#!/usr/bin/python3
"""
Module that contains the State class definition with a relationship to City.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_city import City  # Import City class
from model_state import Base


class State(Base):
    """
    State class that inherits from Base
    """
    __tablename__ = 'states'

    id = Column(
            Integer,
            primary_key=True,
            nullable=False,
            unique=True,
            autoincrement=True
            )
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City",
            backref="state",
            cascade="all, delete-orphan"
            )
