import os
from ...src.types.user import User
from server.src.query import query as q
import pytest


class TestUser:
    @pytest.fixture
    def user_instance(self):
        return User("123", "netid@nyu.edu", "345", "John", "Doe",
                    "1234567890", "https://www.google.com")

    @pytest.fixture
    def user_instance_phone_none(self):
        return User("123", "netid@nyu.edu", "345", "John", "Doe",
                    None, "https://www.google.com")

    @pytest.fixture
    def dict_instance(self):
        return {"uid": "123", "email": "netid@nyu.edu", "aid": "345",
                "fname": "John", "lname": "Doe", "phone": "1234567890",
                "pfp": "https://www.google.com"}

    @pytest.fixture
    def dict_instance_phone_none(self):
        return {"uid": "123", "email": "netid@nyu.edu", "aid": "345",
                "fname": "John", "lname": "Doe",
                "pfp": "https://www.google.com",
                "phone": None}

    @pytest.fixture
    def json_instance(self):
        return '{"uid": "123", "email": "netid@nyu.edu", "aid": "345", \
            "fname": "John", "lname": "Doe", "phone": "1234567890", \
            "pfp": "https://www.google.com"}'

    @pytest.fixture
    def user_and_json_instance(self):
        user = User("123", "netid@nyu.edu", "345", "John", "Doe",
                    "1234567890", "https://www.google.com")
        json = '{"aid": "345", "email": "netid@nyu.edu", "fname": "John", ' + \
            '"lname": "Doe", "pfp": "https://www.google.com", ' + \
            '"phone": "1234567890", "uid": "123"}'
        return user, json

    @pytest.fixture
    def json_instance_no_uid(self):
        return {"email": "netid@nyu.edu", "fname": "John", "lname": "Doe",
                "phone": "1234567890", "pfp": "https://www.google.com"}

    @pytest.fixture
    def json_instance_no_email(self):
        return {"uid": "123", "fname": "John", "lname": "Doe",
                "phone": "1234567890", "pfp": "https://www.google.com"}

    # Test from_json
    def test_from_json(self, json_instance):
        # Test with a valid json string
        json_str = json_instance
        user = User.from_json(json_str)
        assert user.uid == "123"
        assert user.email == "netid@nyu.edu"

    # Test to_dict
    def test_to_dict(self, user_instance):
        # Test with a valid user
        user_dict = user_instance.to_dict()
        assert user_dict["uid"] == "123"
        assert user_dict["email"] == "netid@nyu.edu"

    # Test to_json_str
    def test_to_json_str(self, user_and_json_instance):
        # Test with a valid user
        user, json = user_and_json_instance
        data = user.to_json_str()
        assert data == json

    def test_queries(self, user_instance):
        if os.getenv('CLOUD') == q.LOCAL:
            user_instance.save()
            filters = {'uid': '123'}

            data = User.find_one(filters)
            assert data['email'] == 'netid@nyu.edu'

            data = User.find_all(filters)
            assert type(data) == list
            assert type(data[0]) == dict

            found = User.exists(filters)
            assert found

            count = User.count(filters)
            assert type(count) == int

            User.delete_one(filters)
            assert User.count(filters) == count - 1

            User.delete_all(filters)
            assert User.count(filters) == 0

    def test_insert_where_phone_none(self, dict_instance_phone_none):
        if os.getenv('CLOUD', default=q.LOCAL) == q.LOCAL:
            before = User.count({"uid": "123"})

            User.insert(dict_instance_phone_none)

            after = User.count({"uid": "123"})
            assert before + 1 == after

            User.delete_one({"uid": "123"})
            assert before == User.count({"uid": "123"})

    def test_save_where_phone_none(self, user_instance_phone_none):
        if os.getenv('CLOUD', default=q.LOCAL) == q.LOCAL:
            before = User.count({"uid": "123"})

            user_instance_phone_none.save()

            after = User.count({"uid": "123"})
            assert before + 1 == after

            User.delete_one({"uid": "123"})
            assert before == User.count({"uid": "123"})

    def test_insert_fail_no_uid(self, json_instance_no_uid):
        if os.getenv('CLOUD', default=q.LOCAL) == q.LOCAL:
            with pytest.raises(ValueError):
                data = json_instance_no_uid
                User.insert(data)

    def test_insert_fail_no_email(self, json_instance_no_email):
        if os.getenv('CLOUD', default=q.LOCAL) == q.LOCAL:
            with pytest.raises(ValueError):
                data = json_instance_no_email
                User.insert(data)

    def test_insert_fail_invalid_phone(self, dict_instance):
        if os.getenv('CLOUD', default=q.LOCAL) == q.LOCAL:
            with pytest.raises(ValueError):
                data = dict_instance
                data['phone'] = '12345678901'
                User.insert(data)

    def test_insert_duplicate(self, dict_instance):
        if os.getenv('CLOUD', default=q.LOCAL) == q.LOCAL:
            User.insert(dict_instance)
            filters = {'uid': dict_instance['uid']}
            assert User.count(filters) == 1

            dict_instance['fname'] = 'Will'
            dict_instance['lname'] = 'Smith'
            User.insert(dict_instance)
            assert User.count(filters) == 1

            user = User.find_one(filters)
            assert user['fname'] == 'Will'
            assert user['lname'] == 'Smith'

            User.delete_all()
            assert User.count() == 0
