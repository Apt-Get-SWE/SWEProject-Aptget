from ...src.endpoints.login import GoogleLogIn, LogInSuccessPage
from google_auth_oauthlib.flow import Flow


class TestLogin:
    def test_login_successfully_get_redirecturl(self):
        login = GoogleLogIn()
        redirect = login.get()
        assert 'Redirect URL' in redirect

    def test_login_unsuccessfull(self):
        """
        tests for when client secret file is placed in wrong directory
        """
        login = GoogleLogIn()
        try:
            login.flow.from_client_secrets_file = Flow.from_client_secrets_file(
                client_secrets_file="incorrectfilepath",
                scopes=["https://www.googleapis.com/auth/userinfo.profile",
                        "https://www.googleapis.com/auth/userinfo.email", "openid"],
                redirect_uri="incorrectcallbackuri")
            login.get()
            assert False
        except FileNotFoundError:
            assert True

    def test_loggedin_endpoint(self):
        p = LogInSuccessPage()
        val = p.get()
        assert val['Data']['Login Status'] == {'Login Status': 'Successful'}

    def test_loggedin_failed(self):
        p = LogInSuccessPage()
        assert len(p.ids) == 0
