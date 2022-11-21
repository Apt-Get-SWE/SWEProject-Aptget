import json
from types import SimpleNamespace
from bson import json_util

def parse_json(data):
    return json.loads(json_util.dumps(data))

def json_to_object(data):
    if isinstance(data, dict):
        data = json.dumps(data)
    return json.loads(data, object_hook=lambda d: SimpleNamespace(**d))

def object_to_json_str(obj):
    return json.dumps(obj, default=lambda o: o.__dict__, sort_keys=True)