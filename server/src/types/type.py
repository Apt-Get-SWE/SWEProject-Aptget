from json import loads
from types import SimpleNamespace
from pymongo import MongoClient

def json_to_object(data):
    return loads(data, object_hook=lambda d: SimpleNamespace(**d))

def get_collection(dbname, cname):
    uri = "SECRET"
    client = MongoClient(uri)
    return client[dbname][cname]

class User:
    """
    Insert data to 'users' collection

    data format: {
        'uid'     : int,
        'fname'   : str,
        'lname'   : str,
        'phone'   : str,
        'address' : {
            'building' : str,
            'city'     : str,
            'state'    : str,
            'zip'      : int
        }
    }
    """

    def insert(data):
        users = get_collection('apt-get', 'users')
        users.insert_one(data)

    def __init__(self, data=None):
        self.data = json_to_object(data)
        self.raw_data = data

class Post:
    """
    Insert data to 'posts' collection

    data format: {
        'pid'       : int,
        'title'     : str,
        'details'   : str,
        'condition' : str,
        'list_date' : str,
        'price'     : int,
        'sold'      : boolean
    """
    def insert(data):
        posts = get_collection('apt-get', 'posts')
        posts.insert_one(data)

    def __init__(self, data=None):
        self.data = json_to_object(data)
        self.raw_data = data

    