import pytest
from ...src.types.address import Address


class TestAddress:
    def test_from_json(self):
        # Test with a valid json string
        addr = Address.from_json('{"building": "370 Jay St", "city": "Brooklyn", "state": "NY", "zipcode": "11201"}')
        assert addr.building == "370 Jay St"
        assert addr.city     == "Brooklyn"
        assert addr.state    == "NY"
        assert addr.zipcode  == "11201"

    # Test to_dict
    def test_to_dict(self):
        # Test with a valid address
        addr = Address("370 Jay St", "Brooklyn", "NY", "11201")
        addr_dict = addr.to_dict()
        assert addr_dict["building"] == "370 Jay St"
        assert addr_dict["city"]     == "Brooklyn"
        assert addr_dict["state"]    == "NY"
        assert addr_dict["zipcode"]  == "11201"

    # Test to_json_str
    def test_to_json_str(self):
        # Test with a valid address
        addr = Address("370 Jay St", "Brooklyn", "NY", "11201")
        data = addr.to_json_str()
        assert data == '{"building": "370 Jay St", "city": "Brooklyn", "state": "NY", "zipcode": "11201"}'

    def test_query(self):
        return # CI/CD test don't work w/ localdb

        Address.insert({'test': 'address'}, True)

        res = Address.find_all({}, True)
        assert type(res) == list

        res = Address.find_one({}, True)
        assert type(res) == dict