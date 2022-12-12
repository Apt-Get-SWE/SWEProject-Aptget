import json
from ...app import app


class TestGoogleAPI:
    def testPost(self):
        testapp = app.test_client()
        payload = json.dumps({
            "Request Type": "query",
            "Validate": False,
            'URL': "www.randomurl.com"
        })
        response = testapp.post('http://127.0.0.1:8000/serialize/serialize',
                                headers={"Content-Type": "application/json"}, data=payload)

        assert 200 == response.status_code
        assert b'{"Validate": "false"}\n' == response.data

    def testPostFailDueToIncorrectType(self):
        testapp = app.test_client()
        payload = json.dumps({
            "Request Type": "query",
            "Validate": 'False',
            'URL': "www.randomurl.com"
        })
        response = testapp.post('http://127.0.0.1:8000/serialize/serialize',
                                headers={"Content-Type": "application/json"}, data=payload)
        assert b'{}\n' == response.data
