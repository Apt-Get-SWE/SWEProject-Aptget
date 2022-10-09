from json import loads
from types import SimpleNamespace
from pymongo import MongoClient

def json_to_object(data):
    return loads(data, object_hook=lambda d: SimpleNamespace(**d))

def get_collection(dbname, cname):
    CONNECTION_STRING = "SECRET"
    client = MongoClient(CONNECTION_STRING)
    return client[dbname][cname]

class User:
    def __init__(self, data=None):
        self.data = json_to_object(data)
        self.raw_data = data

    def insert(fname='', lname='', phone='', building='', city='', state='', zipcode=''):
        users = get_collection('apt-get', 'users')
        users.insert_one({
            'uid': users.count_documents({}),
            'fname'   : fname,
            'lname'   : lname,
            'phone'   : phone,
            'address' : {
                'building' : building,
                'city'     : city,
                'state'    : state,
                'zip'      : zipcode
            }
        })

class Post:
    def __init__(self, data=None):
        self.data = json_to_object(data)
        self.raw_data = data

    def insert(title, details, condition, list_date, price, sold):
        posts = get_collection('apt-get', 'posts')
        posts.insert_one({
            'pid': posts.count_documents({}),
            'title'     : title,
            'details'   : details,
            'condition' : condition,
            'list_date' : list_date,
            'price'     : price,
            'sold'      : sold
        })

    