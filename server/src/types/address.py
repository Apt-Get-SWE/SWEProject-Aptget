from ..db import query
from .utils import json_to_object

"""
Address format
{   
    building : str,
    city     : str,
    state    : str, # store abbreviated name, i.e. NY = New York
    zipcode  : str,
}
"""
class Address:
    # STATIC METHODS
    @staticmethod
    def insert(data: dict) -> None:
        if type(data) != dict:
            raise ValueError(f'Cannot insert data of type{type(data)}')
        query.insert('addresses', data)

    @staticmethod
    def find_all(filters={}) -> list:
        return query.find_all('addresses', filters)

    @staticmethod
    def find_one(filters={}) -> dict:
        return query.find_one('addresses', filters)

    # NON-STATIC METHODS
    def __init__(self, data: dict):
        obj = json_to_object(data)
        self.building = obj.building
        self.city     = obj.city
        self.state    = obj.state
        self.zipcode  = obj.zipcode