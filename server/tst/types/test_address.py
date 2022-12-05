from ...src.types.address import Address


class TestAddress:
    def test_from_json(self):
        # Test with a valid json string
        addr = Address.from_json('{"aid": "123", "building": "370 Jay St", "city": "Brooklyn", "state": "NY", "zipcode": "11201"}') # noqa
        assert addr.aid == "123"
        assert addr.building == "370 Jay St"
        assert addr.city == "Brooklyn"
        assert addr.state == "NY"
        assert addr.zipcode == "11201"

    def test_from_raw_addr(self):
        addr = Address.from_json(Address.process_raw_addr(
            "370 Jay St, Brooklyn, NY, 11201"))
        print(addr.building)
        assert addr.building == "370 Jay St"
        assert addr.city == "Brooklyn"
        assert addr.state == "NY"
        assert addr.zipcode == "11201"

    # Test to_dict
    def test_to_dict(self):
        # Test with a valid address
        addr = Address("123", "370 Jay St", "Brooklyn", "NY", "11201")
        addr_dict = addr.to_dict()
        assert addr_dict["aid"] == "123"
        assert addr_dict["building"] == "370 Jay St"
        assert addr_dict["city"] == "Brooklyn"
        assert addr_dict["state"] == "NY"
        assert addr_dict["zipcode"] == "11201"

    # Test to_json_str
    def test_to_json_str(self):
        # Test with a valid address
        addr = Address("123", "370 Jay St", "Brooklyn", "NY", "11201")
        data = addr.to_json_str()
        assert data == '{"aid": "123", "building": "370 Jay St", "city": "Brooklyn", "state": "NY", "zipcode": "11201"}' # noqa

    def test_query(self):
        return  # CI/CD test don't work w/ localdb

        Address.insert({"aid": "123", "building": "370 Jay St",
                       "city": "Brooklyn", "state": "NY", "zipcode": "11201"})

        res = Address.find_all({})
        assert type(res) == list

        res = Address.find_one({})
        assert type(res) == dict
