from ..query import query
from .utils import json_to_object, object_to_json_str

"""
Address format
{   
    aid      : str,
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

    @classmethod
    def from_json(cls, data: str):
        obj = json_to_object(data)
        return cls(obj.building, obj.city, obj.state, obj.zipcode)

    # NON-STATIC METHODS
    def __init__(self, building: str, city: str, state: str, zipcode: str):
        self.building = building
        self.city     = city
        self.state    = state
        self.zipcode  = zipcode

    def to_dict(self):
        # If has an ObjectId, convert to string
        if '_id' in self.__dict__:
            self.__dict__['_id'] = str(self.__dict__['_id'])
        return self.__dict__

    def to_json_str(self):
        return object_to_json_str(self)

    def save(self):
        self.insert(self.__dict__)