from ..query import query
from .utils import json_to_object, object_to_json_str
from datetime import datetime
from pymongo import results
import logging
from uuid import uuid4


class Post:
    """
    Required fields:
    {
        pid         : str
        uid         : str
        aid         : str
        title       : str
        descr       : str
        condition   : str
        list_dt     : str (%m/%d/%Y %H:%M:%S)
        price       : str
        sold        : str
    }
    """

    # TODO: change static methods to stand alone funcitons

    # STATIC METHODS

    @staticmethod
    def insert(data: dict) -> str or None:
        """
        Inserts new Post to database or updates Post if
        same PID is found. A unique PID is generated if none is provided.
        Returns PID of data inserted.

        Arguments:
        data (dict) -- dict containing the Post information
        """

        if 'pid' in data:
            filters = {'pid': data['pid']}
            new_values = {'$set': data}
            Post.update_one(filters, new_values)
        else:
            data['pid'] = str(uuid4())
            query.insert('posts', data)
            logging.info(f'Inserted post {data}')
        return data['pid']

    @staticmethod
    def update_one(filters: dict, new_values: dict) -> None:
        """
        Finds a single Post with the specified filters
        and updates them with new values.

        Arguments:
        filters    -- the Post attributes to search for
        new_values -- the data to be added to the Post

        Exceptions:
        TypeError -- raised if filters or new_values are not of type dict
        """
        if type(filters) != dict:
            raise TypeError(f'Cannot update with filters of type{type(filters)}')  # noqa

        query.update_one('posts', filters, new_values)
        logging.info(f'Updated Posts w/ filters {filters}')

    @staticmethod
    def find_all(filters={}) -> list[dict]:
        """Returns a list of all Posts found with the filters provided ."""
        return query.find_all('posts', filters)

    @staticmethod
    def find_one(filters={}) -> dict:
        """Returns a single Post dict with the filters provided."""
        return query.find_one('posts', filters)

    @staticmethod
    def exists(filters={}) -> bool:
        """Returns true if a Post with the provided filters is found."""
        return query.exists('posts', filters)

    @staticmethod
    def count(filters={}) -> int:
        """Counts all Posts with filters provided."""
        return query.count('posts', filters)

    @staticmethod
    def delete_one(filters={}) -> results.DeleteResult:
        """
        Finds and deletes a single Post with the filters provided.
        Returns the deleted data as a DeleteResult.
        """
        return query.delete_one('posts', filters)

    @staticmethod
    def delete_all(filters={}) -> results.DeleteResult:
        """
        Finds and deletes all Posts with the filters provided.
        Returns the deleted data as a DeleteResult.
        """
        return query.delete_all('posts', filters)

    # CLASS METHODS
    @classmethod
    def from_json(cls, data: str):
        """Creates a Post object from the JSON string provided."""
        obj = json_to_object(data)
        return cls(**obj.__dict__)

    def is_valid(self, **kwargs) -> None:
        """
        Checks if the fields in data are present and valid.
        """
        # check if each field is of correct type
        if 'pid' in kwargs and type(pid := kwargs['pid']) != str:
            raise TypeError(f'pid must be of type str, not {type(pid)}')

        if 'uid' not in kwargs:
            raise ValueError('Post data does not contain uid!')
        elif type(uid := kwargs['uid']) != str:
            raise TypeError(f'uid must be of type str, not {type(uid)}')

        if 'aid' not in kwargs:
            raise ValueError('Post data does not contain aid!')
        elif type(aid := kwargs['aid']) != str:
            raise TypeError(f'aid must be of type str, not {type(aid)}')

        if 'list_dt' not in kwargs:
            raise ValueError('Post data does not include a listing date!')
        else:
            list_dt = kwargs['list_dt']
            if type(list_dt) != str:
                raise TypeError(f'list_dt must be of type str, not {type(list_dt)}')

            try:
                datetime.strptime(list_dt, "%m/%d/%Y %H:%M:%S")
            except ValueError:
                raise ValueError('list_dt must be in format %m/%d/%Y %H:%M:%S')

        if 'price' not in kwargs:
            raise ValueError('Post data must include a price!')
        elif 'price' in kwargs:
            price = kwargs['price']
            try:
                round(float(price), 2)
            except ValueError:
                raise ValueError('Price must be a valid number')

        if 'sold' not in kwargs or kwargs['sold'] not in ["Sold", "Available", "Pending"]:
            raise ValueError('Sold must be one of ["Sold", "Available", "Pending"]')

    # NON-STATIC METHODS
    def __init__(self, **kwargs):
        # TODO: run validation on all fields
        self.is_valid(**kwargs)
        self.pid = kwargs['pid'] if 'pid' in kwargs else str(uuid4())
        self.uid = kwargs['uid']
        self.aid = kwargs['aid']
        self.title = kwargs['title'] if 'title' in kwargs else None
        self.descr = kwargs['descr'] if 'descr' in kwargs else None
        self.image = kwargs['image'] if 'image' in kwargs else None
        self.condition = kwargs['image'] if 'image' in kwargs else None
        self.list_dt = kwargs['list_dt']
        self.price = str(round(float(kwargs['price']), 2))
        self.sold = kwargs['sold']

    def to_dict(self):
        """
        Returns the Post object as a dict.
        Converts ObjectID to a string if found.
        """
        if '_id' in self.__dict__:
            self.__dict__['_id'] = str(self.__dict__['_id'])
        return self.__dict__

    def to_json_str(self):
        """Returns the Post object as a JSON string."""
        return object_to_json_str(self)

    def save(self) -> str or None:
        """
        Inserts Post object to database or updates Post if
        same PID is found.
        Returns auto-generated PID if no duplicate is found.
        """
        if not Post.exists({'pid': self.pid}):
            # if pid not found, generate UUID inside Post.insert()
            data = self.to_dict()
            del data['pid']
            return Post.insert(data)
        else:
            new_vals_dict = {"$set": {}}
            new_vals_dict["$set"]["title"] = self.title
            new_vals_dict["$set"]["descr"] = self.descr
            new_vals_dict["$set"]["image"] = self.image
            new_vals_dict["$set"]["condition"] = self.condition
            new_vals_dict["$set"]["price"] = self.price
            new_vals_dict["$set"]["sold"] = self.sold

            Post.update_one({'pid': self.pid}, new_vals_dict)
