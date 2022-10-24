from server.src.types import address

class TestAddress:
    def test_address(self):
        return # CI/CD tests don't work w/ localdb

        Address.insert({'test': 'address'}, True)

        res = Address.find_all({}, True)
        assert type(res) == list

        res = Address.find_one({}, True)
        assert type(res) == dict