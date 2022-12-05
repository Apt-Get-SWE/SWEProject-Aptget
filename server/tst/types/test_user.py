import os
from ...src.types.user import User

ENV = os.getenv('ENV')


class TestUser:
    # Test from_json
    def test_from_json(self):
        # Test with a valid json string
        json_str = '{"uid": "123", "email": "netid@nyu.edu", "fname": "John", \
            "lname": "Doe", "phone": "1234567890", \
            "pfp": "https://www.google.com"}'
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
        assert json_str == '{"email": "netid@nyu.edu", "fname": "John", ' + \
            '"lname": "Doe", "pfp": "https://www.google.com", ' + \
            '"phone": "1234567890", "uid": "123"}'

    def test_insert_find(self):
        return  # avoid in CI/CD

        if ENV != 'local':
            return

        user = User("123", "netid@nyu.edu", "John", "Doe",
                    "1234567890", "https://www.google.com")
        user.save()

        data = User.find_one({'uid': '123'})
        assert data['email'] == 'netid@nyu.edu'

        data = User.find_all({'uid': '123'})
        assert type(data) == list
        assert type(data[0]) == dict

        found = User.exists({'uid': '123'})
        assert found

        count = User.count({'uid': '123'})
        assert type(count) == int

        User.delete_one({'uid': '123'})
        assert User.count({'uid': '123'}) == count - 1

        User.delete_all({'uid': '123'})
        assert User.count({'uid': '123'}) == 0
