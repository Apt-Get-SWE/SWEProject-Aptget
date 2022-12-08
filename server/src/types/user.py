import logging
from pymongo import results, errors
from ..query import query
from .utils import json_to_object, object_to_json_str

"""
User format
{
    uid   : str,
    fname : str,
    lname : str,
    phone : str,
    email : str,
    pfp   : str
}
UID is the google_id of the user
Email is required for every user
"""


class User:
    # STATIC METHODS
    @staticmethod
    def insert(data: dict) -> None:
        """Creates and inserts a new user into the database

        Args:
            data (dict): A dictionary containing the user's information

        Raises:
            ValueError: If given data is not a dictionary, or if the
                        dictionary does not contain all the required fields
        """
        if type(data) != dict:
            raise ValueError(f'Cannot insert data of type{type(data)}')

        # Assert that data has an email and user id
        if 'email' not in data or 'uid' not in data:
            raise ValueError('Cannot insert user without an email or uid')

        logging.info(f'Inserting user {data}')

        try:
            query.insert('users', data)
            logging.info(f'Inserted user {data} into database')
        except errors.DuplicateKeyError:
            logging.info(f'User with uid {data["uid"]} already exists')

    @staticmethod
    def find_all(filters={}) -> list:
        return query.find_all('users', filters)

    @staticmethod
    def find_one(filters={}) -> dict:
        return query.find_one('users', filters)

    @staticmethod
    def exists(filters={}) -> bool:
        return query.users('users', filters)

    @staticmethod
    def count(filters={}) -> int:
        return query.count('users', filters)

    @staticmethod
    def delete_one(filters={}) -> results.DeleteResult:
        return query.delete_one('users', filters)

    @staticmethod
    def delete_all(filters={}) -> results.DeleteResult:
        return query.delete_all('users', filters)

    # CLASS METHODS
    @classmethod
    def from_json(cls, data: str):
        obj = json_to_object(data)
        return cls(obj.uid, obj.email, obj.fname, obj.lname, obj.phone, obj.pfp)  # noqa

    # NON-STATIC METHODS
    def __init__(self, uid: str, email: str, fname: str = None, lname: str = None, phone: str = None, pfp=None):  # noqa
        self.uid = uid
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.email = email
        self.pfp = pfp

    def to_dict(self):
        # If has an ObjectId, convert to string
        if '_id' in self.__dict__:
            self.__dict__['_id'] = str(self.__dict__['_id'])
        return self.__dict__

    def to_json_str(self):
        return object_to_json_str(self)

    def save(self):
        self.insert(self.__dict__)
