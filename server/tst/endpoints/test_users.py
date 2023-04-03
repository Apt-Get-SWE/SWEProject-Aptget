from ...src.types.user import User
from server.src.query import query as q
import os
import pytest
from server.app import app


class TestUsers:
    @pytest.fixture
    def client(self):
        app.config['TESTING'] = True
        if os.getenv('CLOUD') == q.LOCAL:
            User.delete_all()
        with app.test_client() as client:
            # set client session user_id cookie to 42069
            with client.session_transaction() as sess:
                sess['user_id'] = '42069'

            yield client
        if os.getenv('CLOUD') == q.LOCAL:
            User.delete_all()

    def test_get(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            user1 = User("123", "netid1@nyu.edu", "345", "John", "Doe",
                         "1234567890", "https://www.google.com")
            user2 = User("456", "netid2@nyu.edu", "678", "John", "Doe",
                         "0987654321", "https://www.google.com")

            uid1 = user1.save()
            uid2 = user2.save()

            response = client.get("api/users/users?uid=123&uid=456")
            assert response.status_code == 200

            assert response.json['Data'][uid1]['email'] == "netid1@nyu.edu"
            assert response.json['Data'][uid1]['phone'] == "1234567890"

            assert response.json['Data'][uid2]['email'] == "netid2@nyu.edu"
            assert response.json['Data'][uid2]['phone'] == "0987654321"

            result = User.delete_one({'uid': '123'})
            assert result.deleted_count == 1

            result = User.delete_one({'uid': '456'})
            assert result.deleted_count == 1
