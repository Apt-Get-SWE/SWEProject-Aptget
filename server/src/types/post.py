from ..query import query
from .utils import json_to_object, object_to_json_str
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

    # STATIC METHODS
    @staticmethod
    def insert(data: dict) -> str or None:
        """
        Inserts new Post to database or updates Post if
        same PID is found. A unique PID is generated if none is provided.
        Returns PID of data inserted.

        Arguments:
        data (dict) -- dict containing the Post information

        Exceptions:
        ValueError -- raised if data is not of type dict or if the
                        dictionary does not contain required fields
        """
        if type(data) != dict:
            raise TypeError(f'Cannot insert data of type{type(data)}')

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
        if type(new_values) != dict:
            raise TypeError(f'Cannot update with data of type{type(new_values)}')  # noqa
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
        return cls(obj.pid, obj.uid, obj.aid, obj.title, obj.descr, obj.condition, obj.list_dt, obj.price, obj.sold)  # noqa

    # NON-STATIC METHODS
    def __init__(self, pid: str, uid: str, aid: str, title: str = None,
                 descr: str = None, condition: str = None, list_dt: str = None,
                 price: str = "0", sold: str = "False"):
        self.pid = pid
        self.uid = uid
        self.aid = aid
        self.title = title
        self.descr = descr
        self.condition = condition
        self.list_dt = list_dt
        self.price = price
        self.sold = sold

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
            new_vals_dict["$set"]["condition"] = self.condition
            new_vals_dict["$set"]["price"] = self.price
            new_vals_dict["$set"]["sold"] = self.sold

            Post.update_one({'pid': self.pid}, new_vals_dict)
