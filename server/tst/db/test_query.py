from server.src.db import query as q
from pymongo import collection
import os

os.environ['ENV'] = 'local'

class TestClass:
    def test_getcollection(self):
        return # CI/CD test don't work w/ localdb

        users = q.get_collection('apt-get', 'users')
        assert type(users) == collection.Collection

    def test_insert_findone_delete(self):
        return # CI/CD test don't work w/ localdb

        q.insert('users', {'test':'user'})

        res = q.find_one('users', {'test':'user'})
        assert type(res) == dict

    def test_findall(self):
        return # CI/CD test don't work w/ localdb

        res = q.find_all('users')
        assert type(res) == list