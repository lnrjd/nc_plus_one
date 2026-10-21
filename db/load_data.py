
import json

def load_json_data(filepath):
    with open(filepath) as f:
        data = json.load(f)
    return data