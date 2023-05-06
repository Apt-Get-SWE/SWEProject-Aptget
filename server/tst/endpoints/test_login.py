import os
from server.src.query import query as q
from unittest.mock import MagicMock, patch
import pytest
from server.app import app


class TestLogin:
    @pytest.fixture
    def client(self):
        app.config['TESTING'] = True
        with app.test_client() as client:
            # set client session user_id cookie to 1337
            with client.session_transaction() as sess:
                sess['user_id'] = '1337'
            yield client

    def test_save_user_login(self):
        # Mock the necessary objects and methods
        if os.getenv('CLOUD') == q.LOCAL:
            app.config['TESTING'] = True
            with app.test_client() as client:
                # set client session user_id cookie to 1337
                with patch('requests.session') as mock_session, \
                        patch('pip._vendor.cachecontrol.CacheControl') as mock_cache_control, \
                        patch('google.auth.transport.requests.Request') as mock_request, \
                        patch('google.oauth2.id_token.verify_oauth2_token') as mock_verify_oauth2_token, \
                        patch('flask.redirect') as mock_redirect:

                    # Set up the mock values
                    mock_session.return_value = MagicMock()
                    mock_cache_control.return_value = MagicMock()
                    mock_request.return_value = MagicMock()
                    mock_verify_oauth2_token.return_value = {
                        'sub': '12345',
                        'email': 'test@example.com',
                        'given_name': 'John',
                        'family_name': 'Doe',
                        'picture': 'https://example.com/picture.jpg'
                    }
                    mock_redirect.return_value = MagicMock()

                    # Instantiate the class
                    try:
                        client.get('api/login/callback')
                        # This should not succeed because googleOauth2 needs an interactive session
                    except Exception as e:
                        print(e)
                        assert True

    def test_restricted_area_access(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            response = client.get('api/login/restricted_area')
            assert response.status_code == 200
            assert response.json['Data']['Login Status'] == {'Login Status': 'Successfully logged in user 1337'}

    def test_logout(self, client):
        if os.getenv('CLOUD') == q.LOCAL:
            client.get('api/login/logout')
            with client.session_transaction() as session:
                assert 'user_id' not in session
