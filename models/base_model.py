#!/usr/bin/python3
"""
A class  that defines all common attributes/methods for other classes
"""

from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:

    """
    Class containing attributes and methods
    which serves as a base
    model for other classes

    """
    def __init__(self, *args, **kwargs):
        """ constructor for initialization of BaseModel and  validate kwargs
        Args:
             *args(any): unused
             **kwargs(dict):key/value pairs
        """
        """ Public instance attributes"""
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                setattr(self, key, value)
            self.created_at = datetime.strptime(
                self.created_at, '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(
                self.updated_at, '%Y-%m-%dT%H:%M:%S.%f')

        elif len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        storage.new(self)

    def __str__(self):
        """ A string representation of
        the base model
        """

        return ("[{}} ({}) {}".format(self.__class__.__name__, self.id,
                self.__dict__))

    def save(self):
        """ Changing the base model object and updating it"""

        self.updated_at = datetime.now()
        storage.now

    def to_dict(self):
        """ A dictionary containing attributes of the base model"""

        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return vars(self)
