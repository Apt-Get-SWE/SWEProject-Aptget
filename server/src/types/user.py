import logging
from pymongo import results
from ..query import query
from .utils import json_to_object, object_to_json_str


class User:
    """
    Required fields:
    {
        uid   : str (google_id)
        email : str
        aid   : str
        fname : str
        lname : str
        phone : str
        pfp   : str
    }
    """

    # STATIC METHODS
    @staticmethod
    def is_valid(data) -> None:
        """
        Checks if the fields in data are present and valid.
        """
        if type(data) != dict:
            raise TypeError(f'Cannot insert data of type{type(data)}')

        # Assert that data has an email and user id
        if 'email' not in data or 'uid' not in data:
            raise ValueError('Cannot insert user without an email or UID')

        if data['phone'] != "None" \
            and data['phone'] != None \
            and (len(data['phone']) != 10 or not data['phone'].isnumeric()):  # noqa

            print(data['phone'], type(data["phone"]))
            raise ValueError(f"Invalid phone format {data['phone']}")
        return True

    @staticmethod
    def insert(data: dict) -> None:
        """
        Inserts new User to database or updates User if
        same UID is found.

        Arguments:
        data (dict) -- dict containing the User information
        """

        User.is_valid(data)
        filters = {'uid': data['uid']}
        if User.exists(filters):
            new_values = {"$set": data}
            User.update_one(filters, new_values)
        else:
            query.insert('users', data)
            logging.info(f'Inserted user {data["uid"]}')

    @staticmethod
    def update_one(filters: dict, new_values: dict) -> None:
        """
        Finds a single User with the specified filters
        and updates them with new values.

        Arguments:
        filters    -- the User attributes to search for
        new_values -- the data to be added to the User

        Exceptions:
        TypeError -- raised if filters or new_values are not of type dict
        """
        if type(new_values) != dict:
            raise TypeError(
                f'Cannot update with data of type{type(new_values)}')
        if type(filters) != dict:
            raise TypeError(
                f'Cannot update with filters of type{type(filters)}')
        query.update_one('users', filters, new_values)
        logging.info(f'Updated Users w/ filters {filters}')

    @staticmethod
    def find_all(filters={}) -> list[dict]:
        """Returns a list of all Users found with the filters provided ."""
        return query.find_all('users', filters)

    @staticmethod
    def find_one(filters={}) -> dict:
        """Returns a single User dict with the filters provided."""
        return query.find_one('users', filters)

    @staticmethod
    def exists(filters={}) -> bool:
        """Returns true if a User with the provided filters is found."""
        return query.exists('users', filters)

    @staticmethod
    def count(filters={}) -> int:
        """Counts all Users with filters provided."""
        return query.count('users', filters)

    @staticmethod
    def delete_one(filters={}) -> results.DeleteResult:
        """
        Finds and deletes a single User with the filters provided.
        Returns the deleted data as a DeleteResult.
        """
        return query.delete_one('users', filters)

    @staticmethod
    def delete_all(filters={}) -> results.DeleteResult:
        """
        Finds and deletes all Users with the filters provided.
        Returns the deleted data as a DeleteResult.
        """
        return query.delete_all('users', filters)

    # CLASS METHODS
    @classmethod
    def from_json(cls, data: str):
        """Creates a User object from the JSON string provided."""
        obj = json_to_object(data)
        return cls(obj.uid, obj.email, obj.aid, obj.fname, obj.lname, obj.phone, obj.pfp)  # noqa

    # NON-STATIC METHODS
    def __init__(self, uid: str, email: str, aid: str = None, fname: str = None, lname: str = None, phone: str = None, pfp=None):  # noqa
        self.uid = uid
        self.aid = aid
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.email = email
        self.pfp = pfp

    def to_dict(self):
        """
        Returns the User object as a dict.
        Converts ObjectID to a string if found.
        """
        if '_id' in self.__dict__:
            self.__dict__['_id'] = str(self.__dict__['_id'])
        return self.__dict__

    def to_json_str(self):
        """Returns the User object as a JSON string."""
        return object_to_json_str(self)

    def save(self):
        """
        Inserts User object to database or updates User if
        same UID is found.
        """
        if not User.exists({'uid': self.uid}):
            self.insert(self.to_dict())
        else:
            new_vals_dict = {"$set": {}}
            new_vals_dict["$set"]["aid"] = self.aid
            new_vals_dict["$set"]["fname"] = self.fname
            new_vals_dict["$set"]["lname"] = self.lname
            new_vals_dict["$set"]["phone"] = self.phone
            new_vals_dict["$set"]["email"] = self.email

            User.update_one({'uid': self.uid}, new_vals_dict)
