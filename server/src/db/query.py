import os
from pymongo import MongoClient, collection

COLLECTIONS = ['posts', 'items', 'users', 'addresses']
ENV = os.getenv('ENV') # get local environemnt variable

def get_collection(dbname: str, collection_name: str) -> collection.Collection:
    client = None # to be connect to local/remote MongoDB

    # if local is True, connect to local db, otherwise connect to remote db
    if ENV=='local':
        client = MongoClient('localhost', 27017) # connect to local db on port 27017
    else:
        uri = os.getenv('DB_URI') # get remote db URI
        if uri is None:
            raise ValueError('DB_URI environemnt variable not set!')
        client = MongoClient(uri) # connect to remote db
    
    # get db and specified collection
    return client[dbname][collection_name]

# insert document / JSON object to specified collection
def insert(collection_name: str, data: dict) -> None:
    if collection_name.lower() not in COLLECTIONS:
        raise Exception(f"Cannot insert to '{collection_name}'")
    collection = get_collection('apt-get', collection_name)
    return collection.insert_one(data)

# find all instances of document / JSON object in specified collection
def find_all(collection_name: str, filters) -> list:
    if collection_name.lower() not in COLLECTIONS:
        raise Exception(f"Cannot retrieve from '{collection_name}'")

    # fetch collcction from db & return all desired documents in a list
    collection = get_collection('apt-get', collection_name)
    return list(collection.find(filters))

# find one instance of document / JSON object in specified collection
def find_one(collection_name: str, filters={}) -> dict:
    if collection_name.lower() not in COLLECTIONS:
        raise Exception(f"Cannot retrieve from '{collection_name}'")

    # fetch collection from db & return first instance of desired document
    collection = get_collection('apt-get', collection_name)
    return collection.find_one(filters)

# TODO
def exists():
    ...

# TODO
def count():
    ...

# TODO
def delete_one():
    ...

# TODO
def delete_all():
    ...
