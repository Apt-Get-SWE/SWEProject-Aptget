import flask
from ...src.endpoints.addresses import Addresses


class TestPosts:
    def test_query(self):
        return  # TODO: setup testing local db
        # Test with a valid query
        with flask.Flask(__name__).test_request_context() as flask_context:
            flask_context.request.args = {"zip": "11201"}

            addr = Addresses()
            response = addr.get()
            assert response['Type'] == 'Data'
            assert response['Title'] == 'List of addresses'
            assert response['Data'] is not None

            # Assert zip code is correct
            for aid, addr in response['Data'].items():
                assert addr['zipcode'] == '11201'
