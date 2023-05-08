from ...src.types.post import Post
from server.src.query import query as q
import os
import pytest


class TestPost:
    @pytest.fixture
    def post_instance(self):
        return Post(uid="234", aid="345", list_dt="10/10/2010 10:10:10", price="0", sold="Available")

    @pytest.fixture
    def dict_instance(self):
        return {"uid": "234", "aid": "345",
                "title": "Selling chairs!", "descr": "willing to negotiate",
                "image": '', "condition": "new", "list_dt": "10/29/2022 10:11:53",
                "price": "24.99", "sold": "Available"}

    @pytest.fixture
    def json_instance(self):
        return '{"uid": "234", "aid": "345", \
                 "title": "Selling chairs!", "descr": "willing to negotiate", \
                 "image": "", "condition": "new", "list_dt": "10/29/2022 10:11:53", \
                 "price": "24.99", "sold": "Available"}'

    @pytest.fixture
    def dict_instance_no_pid(self):
        return {"uid": "234", "aid": "345", "title": "Selling chairs!",
                "descr": "willing to negotiate", "image": '', "condition": "new",
                "list_dt": "10/29/2022 10:11:53", "price": "24.99",
                "sold": "Available"}

    @pytest.fixture
    def badtype_instance(self):
        return {1, 2, 3, 4}

    # Test from_json
    def test_post_from_json(self, json_instance):
        # Test with a valid json string
        post = Post.from_json(json_instance)
        assert post.uid == "234"
        assert post.aid == "345"

    # Test to_dict
    def test_post_to_dict(self, post_instance):
        # Test with a valid post
        post_dict = post_instance.to_dict()
        assert post_dict["uid"] == "234"
        assert post_dict["aid"] == "345"

    # Test to_json_str
    def test_post_to_json_str(self, post_instance):
        # Test with a valid post
        json = post_instance.to_json_str()
        assert type(json) == str

    def test_post_query(self, dict_instance_no_pid):
        if os.getenv('CLOUD', default=q.LOCAL) == q.LOCAL:
            pid = Post.insert(dict_instance_no_pid)
            assert Post.count() > 0

            uid, aid = dict_instance_no_pid['uid'], dict_instance_no_pid['aid']
            assert Post.exists({'pid': pid, 'uid': uid, 'aid': aid})

            res = Post.find_all()
            assert type(res) == list

            res = Post.find_one()
            assert type(res) == dict

            Post.delete_all()
            assert Post.count() == 0

    def test_post_insert(self, dict_instance_no_pid):
        if os.getenv('CLOUD') == q.LOCAL:
            data = dict_instance_no_pid
            pid = Post.insert(data)

            filters = {"pid": pid}
            assert Post.count(filters) == 1

            post = Post.find_one(filters)
            assert post['title'] == 'Selling chairs!'

            Post.delete_one(filters)
            assert Post.count(filters) == 0

    def test_post_insert_badtype(self, badtype_instance):
        if os.getenv('CLOUD') == q.LOCAL:
            with pytest.raises(TypeError):
                data = badtype_instance
                assert not isinstance(data, dict)
                Post.insert(data)

    def test_post_insert_duplicate(self, dict_instance_no_pid):
        if os.getenv('CLOUD') == q.LOCAL:
            Post.insert(dict_instance_no_pid)
            filters = {"uid": "234", "aid": "345"}
            assert Post.count(filters) == 1

            copy = {
                "uid": "234",
                "aid": "345",
                "title": "Selling chairs!",
                "descr": "willing to negotiate",
                "condition": "new",
                "list_dt": "10/29/2022 10:11:53",
                "price": "24.99",
                "sold": "Available"
            }
            Post.insert(copy)
            assert Post.count(filters) == 2

            Post.delete_all()
            assert Post.count() == 0

    def test_insert_valid(self, dict_instance):
        if os.getenv('CLOUD') == q.LOCAL:
            Post.insert(dict_instance)
            filters = {'pid': dict_instance['pid']}
            assert Post.count(filters) == 1
            Post.delete_all()
            assert Post.count() == 0

    def test_init_invalid_price(self):
        with pytest.raises(ValueError):
            Post(pid="123", uid='234', aid='345', title='Selling chairs!',
                 price='24k', sold='Available', list_dt='10/29/2022 10:11:53',
                 descr='willing to negotiate', condition='new')

    def test_init_invalid_sold(self):
        with pytest.raises(ValueError):
            Post(pid="123", uid='234', aid='345', title='Selling chairs!',
                 price='24.99', sold='False', list_dt='10/29/2022 10:11:53',
                 descr='willing to negotiate', condition='new')
