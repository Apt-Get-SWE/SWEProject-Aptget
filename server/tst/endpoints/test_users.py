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
            user1 = User("42069", "netid1@nyu.edu", "345", "John", "Doe",
                         "1234567890", "https://www.google.com")

            uid1 = user1.save()

            response = client.get("api/users/users")
            assert response.status_code == 200

            assert response.json['Data'][uid1]['email'] == "netid1@nyu.edu"
            assert response.json['Data'][uid1]['phone'] == "1234567890"


            result = User.delete_one({'uid': '42069'})
            assert result.deleted_count == 1
