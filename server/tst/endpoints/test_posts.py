from ...src.types.post import Post
from server.src.query import query as q
import os
import pytest
from server.app import app


class TestPosts:
    @pytest.fixture
    def client(self):
        app.config['TESTING'] = True
        if os.getenv('CLOUD') == q.LOCAL:
            q.delete_all('posts', {})
        with app.test_client() as client:
            # set client session user_id cookie to 1337
            with client.session_transaction() as sess:
                sess['user_id'] = '1337'

            yield client
        if os.getenv('CLOUD') == q.LOCAL:
            q.delete_all('posts', {})

    def test_get_fail(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            response = client.get('api/posts/posts')
            assert response.status_code == 200
            assert not len(response.json['Data']) > 0

    def test_get(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            newpost = Post('1', '1337', '1', 'Local test first post',
                           'First test descr', 'new', '1668994811', '100', 'False')
            newpost.save()

            response = client.get('api/posts/posts')
            assert response.status_code == 200
            assert len(response.json['Data']) == 1

            assert response.json['Data']['1']['title'] == 'Local test first post'

            # delete the new post
            response = client.delete('api/posts/posts', json={'pid': '1'})
            assert response.status_code == 201, response.json

    def test_post_no_login_fail(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            with client.session_transaction() as sess:
                sess['user_id'] = None

            response = client.post('api/posts/posts', json={
                'pid': '2',
                'uid': '1337',
                'aid': '2',
                'title': 'Local test second post',
                'descr': 'Second test descr',
                'condition': 'new',
                'list_dt': '1668994811',
                'price': '100',
                'sold': 'False',
            })

            assert response.status_code == 401

    def test_post_loggedin_uid_not_match_fail(self, client):
        if os.getenv('CLOUD') == q.LOCAL:

            response = client.post('api/posts/posts', json={
                'pid': '2',
                'uid': '1338',
                'aid': '2',
                'title': 'Local test second post',
                'descr': 'Second test descr',
                'condition': 'new',
                'list_dt': '1668994811',
                'price': '100',
                'sold': 'False',
            })

            assert response.status_code == 401

    def test_post_fail(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            response = client.post('api/posts/posts', json={
                'shoudl': 'fail',
            })
            assert response.status_code == 500

    def test_post(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            response = client.post('api/posts/posts', json={
                'pid': '2',
                'uid': '1337',
                'aid': '2',
                'title': 'Local test second post',
                'descr': 'Second test descr',
                'condition': 'new',
                'list_dt': '1668994811',
                'price': '100',
                'sold': 'False',
            })
            assert response.status_code == 201, response.json
            assert response.json == 'Post created successfully'

            response = client.get('api/posts/posts')

            assert response.status_code == 200
            assert len(response.json['Data']) == 1
            assert response.json['Data']['2']['title'] == 'Local test second post'

            # delete the new post
            response = client.delete('api/posts/posts', json={'pid': '2'})
            assert response.status_code == 201, response.json

    def test_put_fail(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            response = client.post('api/posts/posts', json={
                'should': 'fail',
            })
            assert response.status_code == 500

    def test_put(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            newpost = Post('1', '1337', '1', 'Local test first post',
                           'First test descr', 'new', '1668994811', '100', 'False')
            newpost.save()

            response = client.put('api/posts/posts', json={
                'pid': '1',
                'uid': '1337',
                'aid': '1',
                'title': 'Updated local test first post',
                'descr': 'test descr',
                'condition': 'new',
                'list_dt': '1668994811',
                'price': '100',
                'sold': 'False',
            })
            assert response.status_code == 201, response.json
            assert response.json == 'Post updated successfully'

            response = client.get('api/posts/posts')

            assert response.status_code == 200
            assert len(response.json['Data']) == 1
            assert response.json['Data']['1']['title'] == 'Updated local test first post'

            # delete the new post
            response = client.delete('api/posts/posts', json={'pid': '1'})
            assert response.status_code == 201, response.json

    def test_delete_fail(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            response = client.delete('api/posts/posts', json={'should': 'fail'})
            assert response.status_code == 500

    def test_delete(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            newpost = Post('1', '1337', '1', 'Local test first post',
                           'First test descr', 'new', '1668994811', '100', 'False')
            newpost.save()

            response = client.delete('api/posts/posts', json={'should': 'fail'})
            assert response.status_code == 500

            response = client.delete('api/posts/posts', json={'pid': '1'})
            assert response.status_code == 201, response.json
            assert response.json == 'Post deleted successfully'

            response = client.get('api/posts/posts')

            assert response.status_code == 200
            assert len(response.json['Data']) == 0
