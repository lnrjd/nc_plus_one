
import json
from pathlib import Path


def load_json_data(filename, directory):
    DATA_DIR = Path(__file__).parent/ directory
    with open(f"{DATA_DIR}/{filename}") as f:
        return json.load(f)