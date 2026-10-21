
import json
from pathlib import Path

def load_json_data(filename):
    DATA_DIR = Path(__file__).parent/ "data"
    with open(f"{DATA_DIR}/{filename}") as f:
        return json.load(f)
