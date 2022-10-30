from ..query import query
from .utils import json_to_object

"""
Post format
{
    pid       : int,
    title     : str,
    details   : str,
    condition : str,
    list_date : str,
    price     : int,
    sold      : boolean
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
    
    # NON-STATIC METHODS
    def __init__(self, data: dict):
        obj = json_to_object(data)
        self.pid       = obj.pid
        self.title     = obj.title
        self.details   = obj.details
        self.condition = obj.condition
        self.list_date = obj.list_date
        self.price     = obj.price
        self.sold      = obj.sold