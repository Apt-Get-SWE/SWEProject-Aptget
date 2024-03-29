import pytest
import os
from server.app import app
from server.src.query import query as q
from ...src.types.address import Address
from ...src.types.user import User


class TestAddr:
    @pytest.fixture
    def client(self):
        app.config['TESTING'] = True
        if os.getenv('CLOUD') == q.LOCAL:
            q.delete_all('addresses', {})
        with app.test_client() as client:
            # set client session user_id cookie to 1337
            with client.session_transaction() as sess:
                sess['user_id'] = '1337'

            # Insert a test user in db
            User.insert({
                'uid': '1337',
                'role': 'admin',
                'email': 'admin@test.com',
                'phone': '1234567890'
            })

            yield client
        # Clean up
        if os.getenv('CLOUD') == q.LOCAL:
            q.delete_all('addresses', {})

    def test_query_fail(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            response = client.get('api/addresses/addr')
            assert response.status_code == 200
            assert not len(response.json['Data']) > 0

    def test_query(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            newaddr = Address(building='test bldg', city='test city', state='test state', zipcode='00000')
            aid = newaddr.save()
            assert aid is not None

            response = client.get('api/addresses/addr')
            print(response.json)

            assert response.status_code == 200
            assert response.json['Type'] == 'Data'
            assert response.json['Title'] == 'List of addresses'
            assert response.json['links']['create_address']['url'] == 'http://localhost/api/addresses/addr'
            assert response.json['links']['create_address']['fields']['aid'] == 'Address ID (required)'
            assert isinstance(response.json['Data'], dict)
            assert len(response.json['Data']) > 0

            response = client.delete(f'api/addresses/addr?aid={aid}')
            assert response.status_code == 200

    def test_put(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            newAddr = Address(building='test bldg', city='test city', state='test state', zipcode='00000')
            aid = newAddr.save()
            assert aid is not None

            response = client.put('api/addresses/addr', json={
                "aid": aid,
                "building": "altered bldg",
                "city": "altered city",
                "state": "altered state",
                "zipcode": "00000"
            })
            assert response.status_code == 200
            assert response.json == "Address modified successfully"

            response = client.get('api/addresses/addr')

            assert response.status_code == 200
            assert len(response.json['Data']) == 1
            assert response.json['Data'][aid]['building'] == "altered bldg"
            assert response.json['Data'][aid]['city'] == "altered city"
            assert response.json['Data'][aid]['state'] == "altered state"

            response = client.delete(f'api/addresses/addr?aid={aid}')
            assert response.status_code == 200

    def test_put_fail(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            response = client.put('api/addresses/addr', json={
                'should': 'fail',
            })
            assert response.status_code == 500

    def test_post_and_prefix_query(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            response = client.post('api/addresses/addr', json={
                "aid": "will-be-overwritten",
                "building": "test bldg",
                "city": "test city",
                "state": "test state",
                "zipcode": "00000"
            })
            assert response.status_code == 201
            assert len(response.json) > 0

            response = client.get('api/addresses/addr?addressPrefix=shouldGiveNoResults')
            assert response.status_code == 200
            assert response.json['Type'] == 'Data'
            assert response.json['Title'] == 'List of addresses'
            assert isinstance(response.json['Data'], dict)
            assert len(response.json['Data']) == 0

            response = client.get('api/addresses/addr?addressPrefix=test')
            assert response.status_code == 200
            assert response.json['Type'] == 'Data'
            assert response.json['Title'] == 'List of addresses'
            assert isinstance(response.json['Data'], dict)
            assert len(response.json['Data']) == 1

            aid = list(response.json['Data'].keys())[0]
            response = client.delete(f'api/addresses/addr?aid={aid}')
            assert response.status_code == 200

    def test_post_fail(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            response = client.post('api/addresses/addr')
            assert response.status_code != 201

            response = client.post('api/addresses/addr', data="some illegal message")
            assert response.status_code != 201

    def test_delete_fail(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            response = client.delete('api/addresses/addr?aid=fail')
            assert response.status_code == 400

    def test_delete(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            newAddr = Address(building='test bldg', city='test city', state='test state', zipcode='00000')
            aid = newAddr.save()
            assert aid is not None

            response = client.delete(f'api/addresses/addr?aid={aid}')
            assert response.status_code == 200
            assert response.json == "Address deleted successfully"

            response = client.get('api/addresses/addr')
            assert response.status_code == 200
            assert len(response.json['Data']) == 0

    def test_put_no_changes(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            newAddr = Address(building='test bldg', city='test city', state='test state', zipcode='00000')
            aid = newAddr.save()
            assert aid is not None

            response = client.put('api/addresses/addr', json={
                "aid": aid,
                "building": "test bldg",
                "city": "test city",
                "state": "test state",
                "zipcode": "00000"
            })
            assert response.status_code == 200
            assert response.json == "Address modified successfully"

            response = client.get('api/addresses/addr')

            assert response.status_code == 200
            assert len(response.json['Data']) == 1
            assert response.json['Data'][aid]['building'] == "test bldg"
            assert response.json['Data'][aid]['city'] == "test city"
            assert response.json['Data'][aid]['state'] == "test state"

            response = client.delete(f'api/addresses/addr?aid={aid}')
            assert response.status_code == 200
