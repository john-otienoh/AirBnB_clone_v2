#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel):
    """ State class """
    __table_name__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            'City',
            backref='state', cascade='all, delete-orphan'
        )
    else:
        @property
        def cities(self):
            """"""
            import models
            from models.city import City
            city_list = []
            for i in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(i)
            return city_list
