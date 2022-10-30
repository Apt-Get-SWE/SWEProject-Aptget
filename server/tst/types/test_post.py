import pytest
from ...src.types.post import Post


class TestPost:
    def test_db(self):
        return  # CI/CD test don't work w/ localdb

        Post.insert({'test': 'post'}, True)

        res = Post.find_all({}, True)
        assert type(res) == list

        res = Post.find_one({}, True)
        assert type(res) == dict
