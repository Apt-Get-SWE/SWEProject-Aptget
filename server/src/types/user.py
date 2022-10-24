from ..db import query
from .utils import json_to_object

"""
User format
{
    uid   : str,
    fname : str,
    lname : str,
    phone : str,
    email : str
}
"""
class User:
    # STATIC METHODS
    def insert(data: dict, local=False) -> None:
        if type(data) != dict:
            raise ValueError(f'Cannot insert data of type{type(data)}')
        query.insert('users', data, local)

    def find_all(filters={}, local=False) -> list:
        return query.find_all('users', filters, local)

    def find_one(filters={}, local=False) -> dict:
        return query.find_one('users', filters, local)

    # NON-STATIC METHODS
    def __init__(self, data: dict):
        obj = json_to_object(data)
        self.uid   = obj.uid
        self.fname = obj.fname
        self.lname = obj.lname
        self.phone = obj.phone
        self.email - obj.email
