import json
from types import SimpleNamespace

def json_to_object(data):
    return json.loads(data, object_hook=lambda d: SimpleNamespace(**d))

def object_to_json_str(obj):
    return json.dumps(obj, default=lambda o: o.__dict__, sort_keys=True)