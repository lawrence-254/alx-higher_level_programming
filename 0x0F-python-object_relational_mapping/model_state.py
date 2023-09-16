#!/usr/bin/python3
"""
a python file that contains the class definition of a State and
an instance Base = declarative_base():
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
# establish a path to the database
engine = create_engine('mysql://root:root@localhost:3306/hbtn_0e_6_usa')
# connecting classes to database
Base = declarative_base()


class State(Base):
    """
    inherits fom Base class
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
