from ...src.types.address import Address
from ...src.types.post import Post
from ...src.types.user import User
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
            newpost = Post(uid='1337', aid='1', title='Local test first post',
                           descr='First test descr', image='', condition='new',
                           list_dt='10/29/2022 10:11:53', price='100', sold='Available')
            pid = newpost.save()

            response = client.get('api/posts/posts')
            assert response.status_code == 200
            assert len(response.json['Data']) == 1
            assert response.json['Data'][pid]['title'] == 'Local test first post'

            response = client.get('api/posts/posts?aid=1')
            assert response.status_code == 200
            assert len(response.json['Data']) == 1
            assert response.json['Data'][pid]['title'] == 'Local test first post'

            response = client.get('api/posts/posts?aid=4')
            assert response.status_code == 200
            assert len(response.json['Data']) == 0

            # delete the new post
            response = client.delete(f'api/posts/posts?pid={pid}')
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
                'image': '',
                'condition': 'new',
                'list_dt': '10/29/2022 10:11:53',
                'price': '100',
                'sold': 'Available',
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
            user1 = User("1337", "netid1@nyu.edu", "345", "John", "Doe",
                         "1234567890", "https://www.google.com")
            user1.save()  # save user to db, so /posts can query it for aid

            response = client.post('api/posts/posts', json={
                'pid': '2',
                'uid': '1337',
                'aid': '2',
                'title': 'Local test second post',
                'descr': 'Second test descr',
                'image': '',
                'condition': 'new',
                'list_dt': '10/29/2022 10:11:53',
                'price': '100',
                'sold': 'Available',
            })
            assert response.status_code == 201, response.json
            assert response.json == 'Post created successfully'

            response = client.get('api/posts/posts')

            assert response.status_code == 200
            assert len(response.json['Data']) == 1

            pid = list(response.json['Data'].keys())[0]
            assert response.json['Data'][pid]['title'] == 'Local test second post'

            # delete the new post
            response = client.delete(f'api/posts/posts?pid={pid}')
            assert response.status_code == 201, response.json

            User.delete_all()  # wipe out the user we created

    def test_put_fail(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            response = client.post('api/posts/posts', json={
                'should': 'fail',
            })
            assert response.status_code == 500

    def test_put(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            newpost = Post(uid='1337', aid='1', title='Local test first post',
                           descr='First test descr', image='', condition='new',
                           list_dt='10/29/2022 10:11:53', price='100', sold='Available')
            pid = newpost.save()

            response = client.put('api/posts/posts', json={
                'pid': pid,
                'uid': '1337',
                'aid': '1',
                'title': 'Updated local test first post',
                'descr': 'test descr',
                'image': '',
                'condition': 'new',
                'list_dt': '10/29/2022 10:11:53',
                'price': '100',
                'sold': 'Available',
            })
            assert response.status_code == 201, response.json
            assert response.json == 'Post updated successfully'

            response = client.get('api/posts/posts')

            assert response.status_code == 200
            assert len(response.json['Data']) == 1
            assert response.json['Data'][pid]['title'] == 'Updated local test first post'

            # delete the new post
            response = client.delete(f'api/posts/posts?pid={pid}')
            assert response.status_code == 201, response.json

    def test_delete_fail(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            response = client.delete('api/posts/posts?pid=fail')
            assert response.status_code == 400

    def test_delete(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            newpost = Post(uid='1337', aid='1', title='Local test first post',
                           descr='First test descr', image='', condition='new',
                           list_dt='10/29/2022 10:11:53', price='100', sold='Available')
            pid = newpost.save()

            response = client.delete('api/posts/posts?pid=fail')
            assert response.status_code == 400

            response = client.delete(f'api/posts/posts?pid={pid}')
            assert response.status_code == 201, response.json
            assert response.json == 'Post deleted successfully'

            response = client.get('api/posts/posts')

            assert response.status_code == 200
            assert len(response.json['Data']) == 0


class TestMarketPosts:
    @pytest.fixture
    def client(self):
        app.config['TESTING'] = True
        if os.getenv('CLOUD') == q.LOCAL:
            q.delete_all('posts', {})
            q.delete_all('addresses', {})
        with app.test_client() as client:
            yield client
        if os.getenv('CLOUD') == q.LOCAL:
            q.delete_all('posts', {})
            q.delete_all('addresses', {})

    def test_get_market_posts(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            # Add address with zipcode
            addr = Address(aid='1', building='123 Main St', city='New York', state='NY', zipcode='10001')
            addr.save()

            # Add a post with the corresponding aid
            post = Post(uid='1337', aid='1', title='Post in 10001 zipcode',
                        descr='Test post', image='', condition='new',
                        list_dt='10/29/2022 10:11:53', price='100', sold='Available')
            pid = post.save()

            response = client.get('api/marketposts?zipcode=10001')
            assert response.status_code == 200
            assert len(response.json['posts']) == 1
            assert response.json['posts'][0]['title'] == 'Post in 10001 zipcode'

            # Clean up
            response = client.delete(f'api/posts/posts?pid={pid}')
            assert response.status_code == 201, response.json
            Address.delete(aid='1')
