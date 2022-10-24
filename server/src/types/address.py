from ..db import query
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
    def insert(data: dict, local=False) -> None:
        if type(data) != dict:
            raise ValueError(f'Cannot insert data of type{type(data)}')
        query.insert('posts', data, local)
    
    def find_all(filters={}, local=False) -> list:
        return query.find_all('posts', filters, local)

    def find_one(filters={}, local=False) -> dict:
        return query.find_one('posts', filters, local)
    
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