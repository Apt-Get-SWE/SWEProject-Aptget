from ...src.types.address import Address
from server.src.query import query as q
import os
import pytest


class TestAddress:
    @pytest.fixture
    def from_json(self):
        json = """{"aid":      "123",
                   "building": "370 Jay St",
                   "city":     "Brooklyn",
                   "state":    "NY",
                   "zipcode":  "11201"}"""
        return Address.from_json(json)

    @pytest.fixture
    def from_raw_addr(self):
        raw = "370 Jay St, Brooklyn, NY, 11201"
        return Address.from_json(Address.process_raw_addr(raw))

    @pytest.fixture
    def to_dict(self):
        return Address("123", "370 Jay St", "Brooklyn", "NY", "11201")

    @pytest.fixture
    def to_json_str(self):
        address = Address("123", "370 Jay St", "Brooklyn", "NY", "11201")
        json = '{"aid": "123", "building": "370 Jay St", "city": "Brooklyn", "state": "NY", "zipcode": "11201"}'  # noqa
        return address, json

    @pytest.fixture
    def query(self):
        return {"aid": "123", "building": "370 Jay St",
                "city": "Brooklyn", "state": "NY",
                "zipcode": "11201"}

    @pytest.fixture
    def insert_no_aid(self):
        return {"building": "370 Jay St", "city": "Brooklyn",
                "state": "NY", "zipcode": "11201"}

    @pytest.fixture
    def insert_badtype(self):
        return {1, 2, 3, 4}

    def test_address_from_json(self, from_json):
        # Test with a valid json string
        addr = from_json
        assert addr.aid == "123"
        assert addr.building == "370 Jay St"
        assert addr.city == "Brooklyn"
        assert addr.state == "NY"
        assert addr.zipcode == "11201"

    def test_address_from_raw_addr(self, from_raw_addr):
        addr = from_raw_addr
        assert addr.building == "370 Jay St"
        assert addr.city == "Brooklyn"
        assert addr.state == "NY"
        assert addr.zipcode == "11201"

    # Test to_dict
    def test_address_to_dict(self, to_dict):
        # Test with a valid address
        addr = to_dict
        addr_dict = addr.to_dict()
        assert addr_dict["aid"] == "123"
        assert addr_dict["building"] == "370 Jay St"
        assert addr_dict["city"] == "Brooklyn"
        assert addr_dict["state"] == "NY"
        assert addr_dict["zipcode"] == "11201"

    # Test to_json_str
    def test_address_to_json_str(self, to_json_str):
        # Test with a valid address
        addr, json = to_json_str
        data = addr.to_json_str()

        assert data == json

    def test_address_query(self, query):
        if os.getenv('CLOUD', default=q.LOCAL) == q.LOCAL:
            Address.insert(query)

            res = Address.find_all()
            assert type(res) == list

            res = Address.find_one()
            assert type(res) == dict

            q.delete_all('addresses')

    def test_address_insert_no_aid(self, insert_no_aid):
        with pytest.raises(ValueError):
            data = insert_no_aid
            Address.insert(data)

    def test_address_insert_badtype(self, insert_badtype):
        with pytest.raises(TypeError):
            data = insert_badtype
            assert not isinstance(data, dict)
            Address.insert(data)
