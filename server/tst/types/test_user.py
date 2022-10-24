from server.src.types import user

class TestUser:
    def test_user(self):
        return # CI/CD tests don't work w/ localdb

        User.insert({'test': 'user'}, True)

        res = User.find_all({}, True)
        assert type(res) == list

        res = User.find_one({}, True)
        assert type(res) == dict

