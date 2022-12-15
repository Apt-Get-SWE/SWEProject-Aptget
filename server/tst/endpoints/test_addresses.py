import pytest
import os
from server.app import app
from server.src.query import query as q
from ...src.types.address import Address


class TestAddr:
    @pytest.fixture
    def client(self):
        app.config['TESTING'] = True
        with app.test_client() as client:
            yield client

    def setup(self):
        if os.getenv('CLOUD') == q.LOCAL:
            # insert one test data
            newaddr = Address('0', 'test bldg', 'test city', 'test state', '00000')
            newaddr.save()

    def test_query(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            response = client.get('/addresses/addr')
            assert response.status_code == 200
            assert response.json['Type'] == 'Data'
            assert response.json['Title'] == 'List of addresses'
            assert isinstance(response.json['Data'], dict)
            assert len(response.json['Data']) > 0

    def test_post(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            response = client.post('/addresses/addr', json={
                "aid": "1",
                "building": "test bldg",
                "city": "test city",
                "state": "test state",
                "zipcode": "00000"
            })
            assert response.status_code == 201
            assert response.json == "Address created successfully"

            response = client.post('/addresses/addr')
            assert response.status_code == 415
            assert response.json == "Content-Type not supported!"
