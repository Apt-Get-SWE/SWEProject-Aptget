from server.src.query import query as q
from pymongo import collection, results
import os
import logging

os.environ['ENV'] = 'local'
LOGGER = logging.getLogger(__name__)
TEST_USER = {'test':'user'}

class TestClass:
    def test_getcollection(self):
        return # CI/CD test don't work w/ localdb
        users = q.get_collection('apt-get', 'users')
        assert type(users) == collection.Collection


    def test_insert(self, data=TEST_USER):
        return # CI/CD test don't work w/ localdb
        q.insert('users', data)


    def test_findone(self):
        return # CI/CD test don't work w/ localdb
        if not q.exists('users', TEST_USER):
            self.test_insert(TEST_USER)
        result = q.find_one('users', TEST_USER)
        assert type(result) == dict


    def test_findall(self):
        return # CI/CD test don't work w/ localdb
        if not q.exists('users', TEST_USER):
            self.test_insert(TEST_USER)
        result = q.find_all('users', {})
        assert type(result) == list
    

    def test_exists(self):
        return # CI/CD test don't work w/ localdb
        if not q.exists('users', TEST_USER):
            self.test_insert(TEST_USER)
        return type(q.exists('users', TEST_USER))


    def test_count(self):
        return # CI/CD test don't work w/ localdb
        if not q.exists('users', TEST_USER):
            self.test_insert(TEST_USER)
        result = q.count('users', TEST_USER)
        assert type(result) == int


    def test_delete_one(self):
        return # CI/CD test don't work w/ localdb
        if not q.exists('users', TEST_USER):
            self.test_insert(TEST_USER)
        result = q.delete_one('users', TEST_USER)
        # LOGGER.warning(result.raw_result)
        assert type(result) == results.DeleteResult


    def test_delete_all(self):
        return # CI/CD test don't work w/ localdb
        if not q.exists('users', TEST_USER):
            self.test_insert(TEST_USER)
        result = q.delete_all('users', TEST_USER)
        assert type(result) == results.DeleteResult