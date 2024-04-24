import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):        
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False)
    pasword = Column(String(100), nullable= False)


class Characters(Base):  # Characters --agregation--> Favorites
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    specie = Column(String(50), nullable = False)
    hair_color = Column(String(50), nullable=True)
    eye_color = Column(String(50), nullable=True)


class Planets(Base):  # Planets --agregation--> Favorites
    __tablename__= 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    terrain = Column(String(100), nullable=False)
    population = Column(String, nullable=False)
    gravity = Column(String, nullable=False)

class Vehicles(Base):  # vehicles --agregation--> Favorites
    __tablename__= 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)
    vehicle_class = Column(String(100), nullable=False)
    consumables = Column(String(100), nullable=True)

class Favorites(Base):  # favorites --composition--> user
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    characters = relationship(Characters)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicles = relationship(Vehicles)
    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
