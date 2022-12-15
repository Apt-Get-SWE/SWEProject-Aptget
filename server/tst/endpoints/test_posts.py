from ...src.types.post import Post
from server.src.query import query as q
import os
import pytest
from server.app import app


class TestPosts:
    @pytest.fixture
    def client(self):
        app.config['TESTING'] = True
        with app.test_client() as client:
            yield client

    def test_get_fail(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            response = client.get('/posts/posts')
            assert response.status_code == 200
            assert not len(response.json['Data']) > 0

    def test_get(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            newpost = Post('1', '1', '1', 'Local test first post',
                           'First test descr', 'new', '1668994811', '100', 'False')
            newpost.save()

            response = client.get('/posts/posts')
            assert response.status_code == 200
            assert len(response.json['Data']) == 1

            assert response.json['Data']['1']['title'] == 'Local test first post'

            # delete the new post
            response = client.delete('/posts/posts', json={'pid': '1'})
            assert response.status_code == 201

    def test_post_fail(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            response = client.post('/posts/posts', json={
                'shoudl': 'fail',
            })
            assert response.status_code == 500

    def test_post(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            response = client.post('/posts/posts', json={
                'pid': '2',
                'uid': '2',
                'aid': '2',
                'title': 'Local test second post',
                'descr': 'Second test descr',
                'condition': 'new',
                'list_dt': '1668994811',
                'price': '100',
                'sold': 'False',
            })
            assert response.status_code == 201
            assert response.json == 'Post created successfully'

            response = client.get('/posts/posts')

            assert response.status_code == 200
            assert len(response.json['Data']) == 1
            assert response.json['Data']['2']['title'] == 'Local test second post'

            # delete the new post
            response = client.delete('/posts/posts', json={'pid': '2'})
            assert response.status_code == 201

    def test_put_fail(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            response = client.post('/posts/posts', json={
                'should': 'fail',
            })
            assert response.status_code == 500

    def test_put(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            newpost = Post('1', '1', '1', 'Local test first post',
                           'First test descr', 'new', '1668994811', '100', 'False')
            newpost.save()

            response = client.put('/posts/posts', json={
                'pid': '1',
                'uid': '1',
                'aid': '1',
                'title': 'Updated local test first post',
                'descr': 'test descr',
                'condition': 'new',
                'list_dt': '1668994811',
                'price': '100',
                'sold': 'False',
            })
            assert response.status_code == 201
            assert response.json == 'Post updated successfully'

            response = client.get('/posts/posts')

            assert response.status_code == 200
            assert len(response.json['Data']) == 1
            assert response.json['Data']['1']['title'] == 'Updated local test first post'

            # delete the new post
            response = client.delete('/posts/posts', json={'pid': '1'})
            assert response.status_code == 201

    def test_delete_fail(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            response = client.delete('/posts/posts', json={'should': 'fail'})
            assert response.status_code == 500

    def test_delete(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            newpost = Post('1', '1', '1', 'Local test first post',
                           'First test descr', 'new', '1668994811', '100', 'False')
            newpost.save()

            response = client.delete('/posts/posts', json={'should': 'fail'})
            assert response.status_code == 500

            response = client.delete('/posts/posts', json={'pid': '1'})
            assert response.status_code == 201
            assert response.json == 'Post deleted successfully'

            response = client.get('/posts/posts')

            assert response.status_code == 200
            assert len(response.json['Data']) == 0
