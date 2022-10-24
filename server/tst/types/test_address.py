import pytest
from ...src.types.address import Address


class TestAddress:
    def test_db(self):
            return # CI/CD test don't work w/ localdb

            Address.insert({'test': 'address'}, True)

            res = Address.find_all({}, True)
            assert type(res) == list

            res = Address.find_one({}, True)
            assert type(res) == dict
