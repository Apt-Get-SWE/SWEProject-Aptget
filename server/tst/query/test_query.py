from server.src.query import query as q
from pymongo import collection, results
import os
# import logging

# LOGGER = logging.getLogger(__name__)
# LOGGER.setLevel(logging.INFO)
TEST_USER = {'test': 'user'}
COLLECTION = 'users'


class TestClass:
    def test_getcollection(self):
        if os.getenv('CLOUD') == q.LOCAL:
            collec = q.get_collection(COLLECTION)
            assert type(collec) == collection.Collection

    def test_insert(self, data=TEST_USER):
        if os.getenv('CLOUD') == q.LOCAL:
            q.insert(COLLECTION, data)

    def test_findone(self):
        if os.getenv('CLOUD') == q.LOCAL:
            if not q.exists(COLLECTION, TEST_USER):
                self.test_insert(TEST_USER)
            result = q.find_one(COLLECTION, TEST_USER)
            assert type(result) == dict

    def test_findall(self):
        if os.getenv('CLOUD') == q.LOCAL:
            if not q.exists(COLLECTION, TEST_USER):
                self.test_insert(TEST_USER)
            result = q.find_all(COLLECTION)
            assert type(result) == list

    def test_exists(self):
        if os.getenv('CLOUD') == q.LOCAL:
            if not q.exists(COLLECTION, TEST_USER):
                self.test_insert(TEST_USER)
            return type(q.exists(COLLECTION, TEST_USER))

    def test_count(self):
        if os.getenv('CLOUD') == q.LOCAL:
            if not q.exists(COLLECTION, TEST_USER):
                self.test_insert(TEST_USER)
            result = q.count(COLLECTION, TEST_USER)
            assert type(result) == int

    def test_delete_one(self):
        if os.getenv('CLOUD') == q.LOCAL:
            if not q.exists(COLLECTION, TEST_USER):
                self.test_insert(TEST_USER)
            result = q.delete_one(COLLECTION, TEST_USER)
            # LOGGER.warning(result.raw_result)
            assert type(result) == results.DeleteResult

    def test_delete_all(self):
        if os.getenv('CLOUD') == q.LOCAL:
            if not q.exists(COLLECTION, TEST_USER):
                self.test_insert(TEST_USER)
            result = q.delete_all(COLLECTION, {'test': 'user'})
            assert type(result) == results.DeleteResult
