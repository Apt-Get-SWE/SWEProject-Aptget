import os
from pymongo import MongoClient, collection, results

LOCAL = '0'
CLOUD = '1'
DB_NAME = 'apt-get'
COLLECTIONS = ('posts', 'items', 'users', 'addresses')


def connect_db():
    if os.getenv('CLOUD', LOCAL) == CLOUD:
        user = os.getenv('USER')
        password = os.getenv('PASS')
        if user is None or password is None:
            raise Exception('Remote database credentials not set!')

        return MongoClient(f'mongodb+srv://{user}:{password}@cluster0.os9dia2.mongodb.net/apt-get')  # noqa

    else:
        return MongoClient('localhost', 27017)


def get_collection(collection_name: str) -> collection.Collection:
    if collection_name.lower() not in COLLECTIONS:
        raise Exception(f"Cannot insert to '{collection_name}'")
    client = connect_db()
    return client[DB_NAME][collection_name]


# update document / JSON object to specified collection
def update(collection_name: str, filters: dict, new_values: dict) -> None:
    collection = get_collection(collection_name)
    return collection.update_one(filters, new_values)


# insert document / JSON object to specified collection
def insert(collection_name: str, data: dict) -> None:
    collection = get_collection(collection_name)
    return collection.insert_one(data)


# find all instances of document / JSON object in specified collection
def find_all(collection_name: str, filters={}) -> list:
    # fetch collcction from db & return all desired documents in a list
    collection = get_collection(collection_name)
    return list(collection.find(filters))


# find one instance of document / JSON object in specified collection
def find_one(collection_name: str, filters={}) -> dict:
    # fetch collection from db & return first instance of desired document
    collection = get_collection(collection_name)
    result = collection.find_one(filters)
    return result if result is not None else {}


def exists(collection_name: str, filters={}) -> bool:
    return find_one(collection_name, filters) is not None


def count(collection_name: str, filters={}) -> int:
    collection = get_collection(collection_name)
    return collection.count_documents(filters)


def delete_one(collection_name: str, filters={}) -> results.DeleteResult:
    collection = get_collection(collection_name)
    return collection.delete_one(filters)


def delete_all(collection_name: str, filters={}) -> results.DeleteResult:
    collection = get_collection(collection_name)
    return collection.delete_many(filters)
