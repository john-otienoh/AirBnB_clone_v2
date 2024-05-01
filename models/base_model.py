#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from models import storage
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,  DateTime, String

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=False, default=datetime.now())
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for i, j in kwargs.items():
                if i == 'created_at' or j == 'updated_at':
                    j = datetime.strptime(i, '%Y-%m-%dT%H:%M:%S.%f')
                if i != '__class__' and hasattr(self.__class__, i):
                    setattr(self, i, j)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary.pop('_sa_instance_state')
        return dictionary
    def delete(self):
        """Delete the current instance from the storage (models.storage)
        by calling the method delete
        """
        from models import storage
        storage.delete(self)
