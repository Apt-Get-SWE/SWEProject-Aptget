from ...src.types.address import Address
from server.src.query import query as q
import os
import pytest


class TestAddress:
    @pytest.fixture
    def address_instance(self):
        return Address("123", "370 Jay St", "Brooklyn", "NY", "11201")

    @pytest.fixture
    def post_and_json_instance(self):
        address = Address("123", "370 Jay St", "Brooklyn", "NY", "11201")
        json = '{"aid": "123", "building": "370 Jay St", "city": "Brooklyn", "state": "NY", "zipcode": "11201"}'  # noqa
        return address, json

    @pytest.fixture
    def address_instance_from_json(self):
        json = """{"aid":      "123",
                   "building": "370 Jay St",
                   "city":     "Brooklyn",
                   "state":    "NY",
                   "zipcode":  "11201"}"""
        return Address.from_json(json)

    @pytest.fixture
    def address_instance_from_raw_addr(self):
        raw = "370 Jay St, Brooklyn, NY, 11201"
        return Address.from_json(Address.process_raw_addr(raw))

    @pytest.fixture
    def dict_instance_no_aid(self):
        return {"building": "370 Jay St", "city": "Brooklyn",
                "state": "NY", "zipcode": "11201"}

    @pytest.fixture
    def badtype_instance(self):
        return {1, 2, 3, 4}

    def test_address_from_json(self, address_instance_from_json):
        # Test with a valid json string
        addr = address_instance_from_json
        assert addr.aid == "123"
        assert addr.building == "370 Jay St"
        assert addr.city == "Brooklyn"
        assert addr.state == "NY"
        assert addr.zipcode == "11201"

    def test_address_from_raw_addr(self, address_instance_from_raw_addr):
        addr = address_instance_from_raw_addr
        assert addr.building == "370 Jay St"
        assert addr.city == "Brooklyn"
        assert addr.state == "NY"
        assert addr.zipcode == "11201"

    # Test to_dict
    def test_address_to_dict(self, address_instance):
        # Test with a valid address
        addr_dict = address_instance.to_dict()
        assert addr_dict["aid"] == "123"
        assert addr_dict["building"] == "370 Jay St"
        assert addr_dict["city"] == "Brooklyn"
        assert addr_dict["state"] == "NY"
        assert addr_dict["zipcode"] == "11201"

    # Test to_json_str
    def test_address_to_json_str(self, post_and_json_instance):
        # Test with a valid address
        addr, json = post_and_json_instance
        data = addr.to_json_str()

        assert data == json

    def test_address_query(self, dict_instance_no_aid):
        if os.getenv('CLOUD', default=q.LOCAL) == q.LOCAL:
            Address.insert(dict_instance_no_aid)

            filters = {
                "building": "370 Jay St",
                "city": "Brooklyn",
                "state": "NY",
                "zipcode": "11201"
            }
            assert Address.count(filters) > 0
            assert Address.exists(filters)

            res = Address.find_all()
            assert type(res) == list

            res = Address.find_one()
            assert type(res) == dict

            Address.delete_all()
            assert Address.count() == 0

    def test_address_insert_no_aid(self, dict_instance_no_aid):
        if os.getenv('CLOUD') == q.LOCAL:
            data = dict_instance_no_aid
            Address.insert(data)

            filters = {
                "building": "370 Jay St",
                "city": "Brooklyn",
                "state": "NY",
                "zipcode": "11201"
            }
            assert Address.count(filters) == 1

            Address.delete_one(filters)
            assert Address.count(filters) == 0

    def test_address_insert_badtype(self, badtype_instance):
        if os.getenv('CLOUD') == q.LOCAL:
            with pytest.raises(TypeError):
                data = badtype_instance
                assert not isinstance(data, dict)
                Address.insert(data)

    def test_insert_duplicate(self, dict_instance_no_aid):
        if os.getenv('CLOUD') == q.LOCAL:
            Address.insert(dict_instance_no_aid)
            filters = {
                "building": "370 Jay St",
                "city": "Brooklyn",
                "state": "NY",
                "zipcode": "11201"
            }
            assert Address.count(filters) == 1

            copy = {"building": "370 Jay St", "city": "Brooklyn",
                    "state": "NY", "zipcode": "11201"}
            Address.insert(copy)
            assert Address.count(filters) == 2

            Address.delete_all(filters)
            assert Address.count(filters) == 0
