from server.src.types import post

class TestPost:
    def test_post(self):
        return # CI/CD tests don't work w/ localdb

        Post.insert({'test': 'post'}, True)

        res = Post.find_all({}, True)
        assert type(res) == list

        res = Post.find_one({}, True)
        assert type(res) == dict