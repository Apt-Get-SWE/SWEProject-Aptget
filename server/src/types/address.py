from ..query import query
from .utils import json_to_object, object_to_json_str
from pymongo import results
import usaddress
import json
import logging

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
            raise TypeError(f'Cannot insert data of type{type(data)}')

        # aid is primary key
        if 'aid' not in data:
            raise ValueError('Cannot insert apartment without aid')

        filters = {'aid': data['aid']}
        if Address.exists(filters):
            new_values = {'$set': data}
            Address.update(filters, new_values)
        else:
            query.insert('addresses', data)
            logging.info(f'Inserted address {data}')

    @staticmethod
    def update(filters: dict, new_values: dict) -> None:
        if type(new_values) != dict:
            raise TypeError(f'Cannot update with data of type{type(new_values)}') # noqa
        if type(filters) != dict:
            raise TypeError(f'Cannot update with filters of type{type(filters)}') # noqa

        query.update('addresses', filters, new_values)
        logging.info(f'Updated users w/ filters {filters}')

    @staticmethod
    def find_all(filters={}) -> list:
        return query.find_all('addresses', filters)

    @staticmethod
    def find_one(filters={}) -> dict:
        return query.find_one('addresses', filters)

    @staticmethod
    def exists(filters={}) -> bool:
        return query.exists('addresses', filters)

    @staticmethod
    def count(filters={}) -> int:
        return query.count('addresses', filters)

    @staticmethod
    def delete_one(filters={}) -> results.DeleteResult:
        return query.delete_one('addresses', filters)

    @staticmethod
    def delete_all(filters={}) -> results.DeleteResult:
        return query.delete_all('addresses', filters)

    @staticmethod
    def process_raw_addr(raw: str):
        processed = usaddress.tag(raw)[0]
        addr = {}
        addr["aid"] = ""  # TBD
        addr["building"] = f"{processed['AddressNumber']} {processed['StreetName']} {processed['StreetNamePostType']}"  # noqa
        addr["city"] = processed['PlaceName']
        addr["state"] = processed['StateName']
        addr["zipcode"] = processed['ZipCode']
        return json.dumps(addr)

    @classmethod
    def from_json(cls, data: str):
        obj = json_to_object(data)
        return cls(obj.aid, obj.building, obj.city, obj.state, obj.zipcode)

    # NON-STATIC METHODS
    def __init__(self, aid: str, building: str, city: str, state: str, zipcode: str):  # noqa
        self.aid = aid
        self.building = building
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def to_dict(self):
        # If has an ObjectId, convert to string
        if '_id' in self.__dict__:
            self.__dict__['_id'] = str(self.__dict__['_id'])
        return self.__dict__

    def to_json_str(self):
        return object_to_json_str(self)

    def save(self):
        # check if post already exists
        if not Address.exists({'aid': self.aid}):
            Address.insert(self.to_dict())
        else:
            new_vals_dict = {"$set": {}}
            new_vals_dict["$set"]["building"] = self.building
            new_vals_dict["$set"]["city"] = self.city
            new_vals_dict["$set"]["state"] = self.state
            new_vals_dict["$set"]["zipcode"] = self.zipcode

            Address.update({'aid': self.aid}, new_vals_dict)
