from ...src.types.post import Post
from server.src.query import query as q
import os
import pytest


class TestPost:
    # Test from_json
    def test_from_json(self):
        # Test with a valid json string
        post = Post.from_json(
            '{"pid": "123", "uid": "234", "aid": "345", \
            "title": "Selling chairs!", "descr": "willing to negotiate", \
                 "condition": "new", "list_dt": "10/29/2022 10:11:53", \
                    "price": "24.99", "sold": "False"}')
        assert post.pid == "123"
        assert post.uid == "234"
        assert post.aid == "345"

    # Test to_dict
    def test_to_dict(self):
        # Test with a valid post
        post = Post("123", "234", "345")
        post_dict = post.to_dict()
        assert post_dict["pid"] == "123"
        assert post_dict["uid"] == "234"
        assert post_dict["aid"] == "345"

    # Test to_json_str
    def test_to_json_str(self):
        # Test with a valid post
        post = Post('123', '234', '345', 'Selling chairs!',
                    'willing to negotiate', 'new',
                    '10/29/2022 10:11:53', "24.99", "False")
        data = post.to_json_str()
        assert data == '{"aid": "345", "condition": "new", "descr": "willing to negotiate", "list_dt": "10/29/2022 10:11:53", "pid": "123", "price": "24.99", "sold": "False", "title": "Selling chairs!", "uid": "234"}'  # noqa

    def test_query(self):
        if os.getenv('CLOUD') == q.LOCAL:

            res = Post.find_all()
            assert type(res) == list

            res = Post.find_one()
            assert type(res) == dict

    def test_insert_fail(self):
        with pytest.raises(ValueError):
            data = {"uid": "234", "aid": "345", "title": "Selling chairs!",
                    "descr": "willing to negotiate", "condition": "new",
                    "list_dt": "10/29/2022 10:11:53", "price": "24.99",
                    "sold": "False"}
            Post.insert(data)
