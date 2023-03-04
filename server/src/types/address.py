from ..query import query
from .utils import json_to_object, object_to_json_str
from pymongo import results
from uuid import uuid4
import usaddress
import json
import logging


class Address:
    """
    Required fields:
    {
        aid      : str
        building : str
        city     : str
        state    : str (abbreviated name, i.e. NY = New York)
        zipcode  : str
    }
    """

    # STATIC METHODS
    @staticmethod
    def insert(data: dict) -> str:
        """
        Inserts new Address to database or updates Address if
        same AID is found. A unique AID is generated if none is provided.
        Returns AID of inserted data.

        Arguments:
        data (dict) -- dict containing the Address information

        Exceptions:
        ValueError -- raised if data is not of type dictionary or if the
                        dictionary does not contain required fields
        """

        if type(data) != dict:
            raise TypeError(f'Cannot insert data of type{type(data)}')

        if 'aid' in data:
            filters = {'aid': data['aid']}
            new_values = {'$set': data}
            Address.update_one(filters, new_values)
        else:
            data['aid'] = str(uuid4())
            query.insert('addresses', data)
            logging.info(f'Inserted address {data}')
        return data['aid']

    @staticmethod
    def update_one(filters: dict, new_values: dict) -> None:
        """
        Finds a single Address with the specified filters
        and updates them with new values.

        Arguments:
        filters    -- the Address attributes to search for
        new_values -- the data to be added to the Address

        Exceptions:
        TypeError -- raised if filters or new_values are not of type dict
        """
        if type(new_values) != dict:
            raise TypeError(f'Cannot update with data of type{type(new_values)}')  # noqa
        if type(filters) != dict:
            raise TypeError(f'Cannot update with filters of type{type(filters)}')  # noqa

        query.update_one('addresses', filters, new_values)
        logging.info(f'Updated Addresses w/ filters {filters}')

    @staticmethod
    def find_all(filters={}) -> list:
        """Returns a list of all Addresss found with the filters provided ."""
        return query.find_all('addresses', filters)

    @staticmethod
    def find_one(filters={}) -> dict:
        """Returns a single Address dict with the filters provided."""
        return query.find_one('addresses', filters)

    @staticmethod
    def exists(filters={}) -> bool:
        """Counts all Addresses with filters provided."""
        return query.exists('addresses', filters)

    @staticmethod
    def count(filters={}) -> int:
        """Counts all Addresses with filters provided."""
        return query.count('addresses', filters)

    @staticmethod
    def delete_one(filters={}) -> results.DeleteResult:
        """
        Finds and deletes a single Address with the filters provided.
        Returns the deleted data as a DeleteResult.
        """
        return query.delete_one('addresses', filters)

    @staticmethod
    def delete_all(filters={}) -> results.DeleteResult:
        """
        Finds and deletes all Addresss with the filters provided.
        Returns the deleted data as a DeleteResult.
        """
        return query.delete_all('addresses', filters)

    @staticmethod
    def process_raw_addr(raw: str):
        """Converts raw address data to a JSON string."""
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
        """Creates an Address object from the JSON string provided."""
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
        """
        Returns the Address object as a dict.
        Converts ObjectID to a string if found.
        """
        # If has an ObjectId, convert to string
        if '_id' in self.__dict__:
            self.__dict__['_id'] = str(self.__dict__['_id'])
        return self.__dict__

    def to_json_str(self):
        """Returns the Address object as a JSON string."""
        return object_to_json_str(self)

    def save(self):
        """
        Inserts Address object to database or updates Address if
        same AID is found.
        Returns auto-generated AID if no duplicate found.
        """
        # check if post already exists
        if not Address.exists({'aid': self.aid}):
            data = self.to_dict()
            del data['aid']
            return Address.insert(data)
        else:
            new_vals_dict = {"$set": {}}
            new_vals_dict["$set"]["building"] = self.building
            new_vals_dict["$set"]["city"] = self.city
            new_vals_dict["$set"]["state"] = self.state
            new_vals_dict["$set"]["zipcode"] = self.zipcode

            Address.update_one({'aid': self.aid}, new_vals_dict)
