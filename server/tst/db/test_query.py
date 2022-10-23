from server.src.db import query as q
from pymongo import collection

class TestClass:
    def test_getcollection(self):
        users = q.get_collection('apt-get', 'users', True)
        assert type(users) == collection.Collection

    def test_insert_findone_delete(self):
        q.insert('users', {'test':'user'}, True)

        res = q.find_one('users', {'test':'user'}, True)
        assert type(res) == dict

    def test_findall(self):
        res = q.find_all('users', local=True)
        assert type(res) == list