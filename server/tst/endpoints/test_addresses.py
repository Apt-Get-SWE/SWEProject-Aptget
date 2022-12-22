import pytest
import os
from server.app import app
from server.src.query import query as q
from ...src.types.address import Address


class TestAddr:
    @pytest.fixture
    def client(self):
        app.config['TESTING'] = True
        if os.getenv('CLOUD') == q.LOCAL:
            q.delete_all('addresses', {})
        with app.test_client() as client:
            yield client
        # Clean up
        if os.getenv('CLOUD') == q.LOCAL:
            q.delete_all('addresses', {})

    def test_query_fail(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            response = client.get('/addresses/addr')
            assert response.status_code == 200
            assert not len(response.json['Data']) > 0

    def test_query(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            newaddr = Address('0', 'test bldg', 'test city', 'test state', '00000')
            newaddr.save()

            response = client.get('/addresses/addr')
            assert response.status_code == 200
            assert response.json['Type'] == 'Data'
            assert response.json['Title'] == 'List of addresses'
            assert isinstance(response.json['Data'], dict)
            assert len(response.json['Data']) > 0

    def test_post(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            response = client.post('/addresses/addr', json={
                "aid": "0",
                "building": "test bldg",
                "city": "test city",
                "state": "test state",
                "zipcode": "00000"
            })
            assert response.status_code == 201
            assert response.json == "Address created successfully"

    def test_post_fail(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            response = client.post('/addresses/addr')
            assert response.status_code != 201

            response = client.post('/addresses/addr', data="some illegal message")
            assert response.status_code != 201
