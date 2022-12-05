from ..query import query
from .utils import json_to_object, object_to_json_str

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
    def insert(data: dict) -> None:
        if type(data) != dict:
            raise ValueError(f'Cannot insert data of type{type(data)}')
        query.insert('posts', data)

    @staticmethod
    def find_all(filters={}) -> list:
        return query.find_all('posts', filters)

    @staticmethod
    def find_one(filters={}) -> dict:
        return query.find_one('posts', filters)

    # CLASS METHODS
    @classmethod
    def from_json(cls, data: str):
        obj = json_to_object(data)
        return cls(obj.pid, obj.uid, obj.aid, obj.title, obj.descr, obj.condition, obj.list_dt, obj.price, obj.sold) # noqa

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
        self.insert(self.__dict__)
