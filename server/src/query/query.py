import os
from pymongo import MongoClient, collection, results


COLLECTIONS = ['posts', 'items', 'users', 'addresses']
ENV = os.getenv('ENV')  # get local environemnt variable


def get_collection(dbname: str, collection_name: str) -> collection.Collection:
    validate(collection_name)
    client = None  # to be connect to local/remote MongoDB

    # if local is True, connect to local db, otherwise connect to remote db
    if ENV == 'local':
        # connect to local db on port 27017
        client = MongoClient('localhost', 27017)
    else:
        uri = os.getenv('DB_URI')  # get remote db URI
        if uri is None:
            raise ValueError('DB_URI environment variable not set!')
        client = MongoClient(uri)  # connect to remote db

    # get db and specified collection
    return client[dbname][collection_name]


def validate(collection_name):
    if collection_name.lower() not in COLLECTIONS:
        raise Exception(f"Cannot insert to '{collection_name}'")

# insert document / JSON object to specified collection


def insert(collection_name: str, data: dict) -> None:
    validate(collection_name)
    collection = get_collection('apt-get', collection_name)
    return collection.insert_one(data)


# find all instances of document / JSON object in specified collection
def find_all(collection_name: str, filters) -> list:
    validate(collection_name)

    # fetch collcction from db & return all desired documents in a list
    collection = get_collection('apt-get', collection_name)
    return list(collection.find(filters))


# find one instance of document / JSON object in specified collection
def find_one(collection_name: str, filters={}) -> dict:
    validate(collection_name)

    # fetch collection from db & return first instance of desired document
    collection = get_collection('apt-get', collection_name)
    return collection.find_one(filters)


def exists(collection_name: str, filters={}) -> bool:
    validate(collection_name)
    return find_one('users', filters) is not None


def count(collection_name: str, filters={}) -> int:
    validate(collection_name)
    collection = get_collection('apt-get', 'users')
    return collection.count_documents(filters)


def delete_one(collection_name: str, filters={}) -> results.DeleteResult:
    validate(collection_name)
    collection = get_collection('apt-get', 'users')
    return collection.delete_one(filters)


def delete_all(collection_name: str, filters={}) -> results.DeleteResult:
    validate(collection_name)
    collection = get_collection('apt-get', 'users')
    return collection.delete_many(filters)
