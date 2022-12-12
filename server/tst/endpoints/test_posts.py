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

    def setup(self):
        if os.getenv('LOCAL') == q.LOCAL:
            # insert one test data
            newpost = Post('1', '1', '1', 'test title', 'test descr', 'new', '1668994811', '100', 'False')
            newpost.save()
        else:
            assert False  # only run test with local db

    def test_query(self, client):
        response = client.get('/posts/posts')
        assert response.status_code == 200
        assert response.json == {
            'Type': 'Data',
            'Title': 'List of posts',
            'Data': {
                'posts': [
                    {
                        'pid': '1',
                        'uid': '1',
                        'aid': '1',
                        'title': 'test title',
                        'descr': 'test descr',
                        'condition': 'new',
                        'list_dt': '1668994811',
                        'price': '100',
                        'sold': 'False',
                    }
                ]
            }
        }

    def test_post(self, client):
        response = client.post('/posts/posts', json={
            'pid': '2',
            'uid': '2',
            'aid': '2',
            'title': 'test title',
            'descr': 'test descr',
            'condition': 'new',
            'list_dt': '1668994811',
            'price': '100',
            'sold': 'False',
        })
        assert response.status_code == 201
        assert response.json == 'Post created successfully'

        response = client.get('/posts/posts')
        assert response.status_code == 200
        assert response.json == {
            'Type': 'Data',
            'Title': 'List of posts',
            'Data': {
                'posts': [
                    {
                        'pid': '1',
                        'uid': '1',
                        'aid': '1',
                        'title': 'test title',
                        'descr': 'test descr',
                        'condition': 'new',
                        'list_dt': '1668994811',
                        'price': '100',
                        'sold': 'False',
                    },
                    {
                        'pid': '2',
                        'uid': '2',
                        'aid': '2',
                        'title': 'test title',
                        'descr': 'test descr',
                        'condition': 'new',
                        'list_dt': '1668994811',
                        'price': '100',
                        'sold': 'False',
                    }
                ]
            }
        }

        # delete the new post
        response = client.delete('/posts/posts', json={'pid': '2'})

    def test_put(self, client):
        response = client.put('/posts/posts', json={
            'pid': '1',
            'uid': '1',
            'aid': '1',
            'title': 'test title updated',
            'descr': 'test descr',
            'condition': 'new',
            'list_dt': '1668994811',
            'price': '100',
            'sold': 'False',
        })
        assert response.status_code == 200
        assert response.json == 'Post updated successfully'

        response = client.get('/posts/posts')
        assert response.status_code == 200
        assert response.json == {
            'Type': 'Data',
            'Title': 'List of posts',
            'Data': {
                'posts': [
                    {
                        'pid': '1',
                        'uid': '1',
                        'aid': '1',
                        'title': 'test title updated',
                        'descr': 'test descr',
                        'condition': 'new',
                        'list_dt': '1668994811',
                        'price': '100',
                        'sold': 'False',
                    }
                ]
            }
        }

    def test_delete(self, client):
        response = client.delete('/posts/posts', json={'pid': '1'})
        assert response.status_code == 200
        assert response.json == 'Post deleted successfully'

        response = client.get('/posts/posts')
        assert response.status_code == 200
        assert response.json == {
            'Type': 'Data',
            'Title': 'List of posts',
            'Data': {
                'posts': []
            }
        }
