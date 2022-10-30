import pytest
from ...src.types.user import User


class TestUser:
    # Test from_json
    def test_from_json(self):
        # Test with a valid json string
        json_str = '{"uid": "123", "email": "netid@nyu.edu", "fname": "John", "lname": "Doe", "phone": "1234567890", "pfp": "https://www.google.com"}'
        user = User.from_json(json_str)
        assert user.uid == "123"
        assert user.email == "netid@nyu.edu"

    # Test to_dict
    def test_to_dict(self):
        # Test with a valid user
        user = User("123", "netid@nyu.edu")
        user_dict = user.to_dict()
        assert user_dict["uid"] == "123"
        assert user_dict["email"] == "netid@nyu.edu"

    # Test to_json_str
    def test_to_json_str(self):
        # Test with a valid user
        user = User("123", "netid@nyu.edu", "John", "Doe",
                    "1234567890", "https://www.google.com")
        json_str = user.to_json_str()
        assert json_str == '{"email": "netid@nyu.edu", "fname": "John", "lname": "Doe", "pfp": "https://www.google.com", "phone": "1234567890", "uid": "123"}'

    def test_query(self):
        return  # CI/CD test don't work w/ localdb

        User.insert({'test': 'user'}, True)

        res = User.find_all({}, True)
        assert type(res) == list

        res = User.find_one({}, True)
        assert type(res) == dict
