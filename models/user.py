#!/usr/bin/python3
"""
Inherits from Basemodel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """ the class user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
