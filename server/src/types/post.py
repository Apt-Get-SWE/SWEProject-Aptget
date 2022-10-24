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
    def insert(data: dict, local=False) -> None:
        if type(data) != dict:
            raise ValueError(f'Cannot insert data of type{type(data)}')
        query.insert('addresses', data, local)

    def find_all(filters={}, local=False) -> list:
        return query.find_all('addresses', filters, local)

    def find_one(filters={}, local=False) -> dict:
        return query.find_one('addresses', filters, local)

    # NON-STATIC METHODS
    def __init__(self, data: dict):
        obj = json_to_object(data)
        self.building = obj.building
        self.city     = obj.city
        self.state    = obj.state
        self.zipcode  = obj.zipcode