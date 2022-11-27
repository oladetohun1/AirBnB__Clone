#!/usr/bin/python3
"""
Inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """The City class"""
    state_id = ""
    name = ""
