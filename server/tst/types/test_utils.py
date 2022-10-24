from ...src.types.utils import json_to_object, object_to_json_str

class TestUtils:
    # Test json_to_object
    def test_json_to_object(self):
        # Test with a valid json string
        json_str = '{"uid": "123", "email": "netid@nyu.edu"}'
        obj = json_to_object(json_str)
        assert obj.uid == "123"
        assert obj.email == "netid@nyu.edu"

    # Test object_to_json_str
    def test_object_to_json_str(self):
        # Test with a valid object
        json_str = '{"email": "netid@nyu.edu", "uid": "123"}' # keys in sorted order
        obj = json_to_object(json_str)
        assert object_to_json_str(obj) == json_str