
import sys
import json
from types import SimpleNamespace
sys.path.insert(0, "../")
from db import query

def json_to_object(data):
    return json.loads(data, object_hook=lambda d: SimpleNamespace(**d))

"""
User format
{
    uid   : str,
    fname : str,
    lname : str,
    phone : str,
    email : str
}
"""
class User:
    # STATIC METHODS
    def insert(data: dict) -> None:
        if type(data) != dict:
            raise ValueError(f'Cannot insert data of type{type(data)}')
        query.insert('users', data)

    # NON-STATIC METHODS
    def __init__(self, data: dict):
        obj = json_to_object(data)
        self.uid   = obj.uid
        self.fname = obj.fname
        self.lname = obj.lname
        self.phone = obj.phone
        self.email - obj.email

"""
Address format
{   
    building : str,
    city     : str,
    state    : str, # store abbreviated name, i.e. NY = New York
    zipcode  : str,
}
"""
class Address:
    # STATIC METHODS
    def insert(data: dict) -> None:
        if type(data) != dict:
            raise ValueError(f'Cannot insert data of type{type(data)}')
        query.insert('addresses', data)

    # NON-STATIC METHODS
    def __init__(self, data: dict):
        obj = json_to_object(data)
        self.building = obj.building
        self.city     = obj.city
        self.state    = obj.state
        self.zipcode  = obj.zipcode

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
    def insert(data: dict) -> None:
        if type(data) != dict:
            raise ValueError(f'Cannot insert data of type{type(data)}')
        query.insert('posts', data)
    
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