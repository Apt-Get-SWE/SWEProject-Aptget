from server.src.query import query as q
from pymongo import collection, results, ASCENDING, errors
import pytest
import os
# import logging

# LOGGER = logging.getLogger(__name__)
# LOGGER.setLevel(logging.INFO)
TEST_USER = {'test': 'user'}
COLLECTION = 'users'
INVALID_COLLECTION = 'names'


class TestClass:
    def test_getcollection(self):
        if os.getenv('CLOUD') == q.LOCAL:
            collec = q.get_collection(COLLECTION)
            assert type(collec) == collection.Collection

    def test_getcollection_fail(self):
        if os.getenv('CLOUD') == q.LOCAL:
            with pytest.raises(Exception):
                q.get_collection(INVALID_COLLECTION)

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

    def test_create_index_all(self):
        if os.getenv('CLOUD') == q.LOCAL:
            q.create_index(COLLECTION, [('uid', ASCENDING)], unique=True)

            user1 = {"uid": 123, "fname": "Tom", "lname": "Zhang"}
            user2 = {"uid": 123, "fname": "Phil", "lname": "Jackson"}

            before = q.count(COLLECTION)
            with pytest.raises(errors.DuplicateKeyError):
                q.insert(COLLECTION, user1)
                q.insert(COLLECTION, user2)

            user2["uid"] = 456
            q.insert(COLLECTION, user2)

            assert q.count(COLLECTION) - before == 2
            q.delete_one(COLLECTION, {"uid": 123})
            q.delete_one(COLLECTION, {"uid": 456})
