from server.src.types.types import User, Address, Post

class TestClass:
    def test_user(self):
        User.insert({'test': 'user'}, True)

        res = User.find_all({}, True)
        assert type(res) == list

        res = User.find_one({}, True)
        assert type(res) == dict

    def test_address(self):
        Address.insert({'test': 'address'}, True)

        res = Address.find_all({}, True)
        assert type(res) == list

        res = Address.find_one({}, True)
        assert type(res) == dict

    def test_post(self):
        Post.insert({'test': 'post'}, True)

        res = Post.find_all({}, True)
        assert type(res) == list

        res = Post.find_one({}, True)
        assert type(res) == dict
