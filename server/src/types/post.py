from ..query import query
from .utils import json_to_object, object_to_json_str
from pymongo import results

"""
Post format
{
    pid         : str,
    uid         : str
    aid         : str,
    title       : str,
    descr       : str
    condition   : str,
    list_dt     : str (%m/%d/%Y %H:%M:%S),
    price       : str,
    sold        : str
}
"""


class Post:
    # STATIC METHODS
    @staticmethod
    def update(filters: dict, new_values: dict) -> None:
        if type(new_values) != dict:
            raise TypeError(f'Cannot update with data of type{type(new_values)}')  # noqa
        if type(filters) != dict:
            raise TypeError(f'Cannot update with filters of type{type(filters)}')  # noqa\
        query.update('posts', filters, new_values)

    @staticmethod
    def insert(data: dict) -> None:
        if type(data) != dict:
            raise TypeError(f'Cannot insert data of type{type(data)}')

        # pid is primary key
        if 'pid' not in data:
            raise ValueError('Cannot insert post without pid')
        query.insert('posts', data)

    @staticmethod
    def find_all(filters={}) -> list:
        return query.find_all('posts', filters)

    @staticmethod
    def find_one(filters={}) -> dict:
        return query.find_one('posts', filters)

    @staticmethod
    def delete(pid) -> results.DeleteResult:
        return query.delete_one('posts', {'pid': pid})

    @staticmethod
    def delete_all(filters={}) -> results.DeleteResult:
        return query.delete_all('posts', filters)

    # CLASS METHODS
    @classmethod
    def from_json(cls, data: str):
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
        # If has an ObjectId, convert to string
        if '_id' in self.__dict__:
            self.__dict__['_id'] = str(self.__dict__['_id'])
        return self.__dict__

    def to_json_str(self):
        return object_to_json_str(self)

    def save(self):
        # check if post already exists
        if not Post.find_one({'pid': self.pid}):
            Post.insert(self.__dict__)
        else:
            new_vals_dict = {"$set": {}}
            new_vals_dict["$set"]["title"] = self.title
            new_vals_dict["$set"]["descr"] = self.descr
            new_vals_dict["$set"]["condition"] = self.condition
            new_vals_dict["$set"]["price"] = self.price
            new_vals_dict["$set"]["sold"] = self.sold

            Post.update({'pid': self.pid}, new_vals_dict)
