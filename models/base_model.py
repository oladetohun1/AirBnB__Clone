#!/usr/bin/python3
"""
A class  that defines all common attributes/methods for other classes
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Class containing attributes and methods
    which serves as a base
    model for other classes
    """
    def __init__(self):
        """ Public instance attributes"""

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ A string representation of
        the base model
        """

        return ("[{}} ({}) {}"
                .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ Changing the base model object and updating it"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """ A dictionary containing attributes of the base model"""

        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return vars(self)
