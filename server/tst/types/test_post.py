from ...src.types.post import Post
from server.src.query import query as q
import os
import pytest


class TestPost:
    @pytest.fixture
    def from_json(self):
        return '{"pid": "123", "uid": "234", "aid": "345", \
                 "title": "Selling chairs!", "descr": "willing to negotiate", \
                 "condition": "new", "list_dt": "10/29/2022 10:11:53", \
                 "price": "24.99", "sold": "False"}'

    @pytest.fixture
    def to_dict(self):
        return Post("123", "234", "345")

    @pytest.fixture
    def to_json_str(self):
        post = Post('123', '234', '345', 'Selling chairs!',
                    'willing to negotiate', 'new',
                    '10/29/2022 10:11:53', "24.99", "False")
        json = '{"aid": "345", "condition": "new", "descr": "willing to negotiate", "list_dt": "10/29/2022 10:11:53", "pid": "123", "price": "24.99", "sold": "False", "title": "Selling chairs!", "uid": "234"}'  # noqa
        return post, json

    @pytest.fixture
    def query(self):
        return {'pid': '123', 'uid': '456', 'aid': '789'}

    @pytest.fixture
    def insert_no_pid(self):
        return {"uid": "234", "aid": "345", "title": "Selling chairs!",
                "descr": "willing to negotiate", "condition": "new",
                "list_dt": "10/29/2022 10:11:53", "price": "24.99",
                "sold": "False"}

    @pytest.fixture
    def insert_badtype(self):
        return {1, 2, 3, 4}

    # Test from_json
    def test_post_from_json(self, from_json):
        # Test with a valid json string
        post = Post.from_json(from_json)
        assert post.pid == "123"
        assert post.uid == "234"
        assert post.aid == "345"

    # Test to_dict
    def test_post_to_dict(self, to_dict):
        # Test with a valid post
        post = to_dict
        post_dict = post.to_dict()
        assert post_dict["pid"] == "123"
        assert post_dict["uid"] == "234"
        assert post_dict["aid"] == "345"

    # Test to_json_str
    def test_post_to_json_str(self, to_json_str):
        # Test with a valid post
        post, json = to_json_str
        data = post.to_json_str()
        assert data == json

    def test_post_query(self, query):
        if os.getenv('CLOUD', default=q.LOCAL) == q.LOCAL:
            print(q.LOCAL)
            Post.insert(query)

            res = Post.find_all()
            assert type(res) == list

            res = Post.find_one()
            assert type(res) == dict

            Post.delete_all()

    def test_post_insert_no_pid(self, insert_no_pid):
        with pytest.raises(ValueError):
            data = insert_no_pid
            Post.insert(data)

    def test_post_insert_badtype(self, insert_badtype):
        with pytest.raises(TypeError):
            data = insert_badtype
            assert not isinstance(data, dict)
            Post.insert(data)
