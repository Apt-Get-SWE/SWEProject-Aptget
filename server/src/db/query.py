import os
from pymongo import MongoClient, collection

COLLECTIONS = ['posts', 'items', 'users', 'addresses']

def get_collection(dbname: str, collection_name: str) -> collection.Collection:
    uri = os.getenv('DB_URI')
    if uri is None:
        raise ValueError('DB_URI environemnt variable not set!')
    client = MongoClient(uri)
    return client[dbname][collection_name]

def insert(collection_name: str, data: dict) -> None:
    if collection_name.lower() not in COLLECTIONS:
        raise Exception(f"Cannot insert to '{collection_name}'")
    collection = get_collection('apt-get', collection_name)
    collection.insert_one(data)

def find_all(collection_name: str, filters={}) -> list:
    if collection_name.lower() not in COLLECTIONS:
        raise Exception(f"Cannot retrieve from '{collection_name}'")
    collection = get_collection('apt-get', collection_name)
    return list(collection.find(filters))

def find_one(collection_name: str, filters={}) -> dict:
    if collection_name.lower() not in COLLECTIONS:
        raise Exception(f"Cannot retrieve from '{collection_name}'")
    collection = get_collection('apt-get', collection_name)
    return collection.find_one(filters)
    