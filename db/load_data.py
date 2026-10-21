
import json

def load_json_data(filepath):
    with open(filepath) as f:
        return json.load(f)
