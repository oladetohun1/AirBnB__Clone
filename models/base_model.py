#!/usr/bin/python3
"""
A class  that defines all common attributes/methods for other classes
"""

from uuid import uuid4
from datetime import datetime

class BaseModel:
    """
    Class containing attributes and methods which serves as a base model for other classes
    """
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return ("[{}} ({}) {}".format(self.class.name, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        for k, v in self.__dict__.items():


