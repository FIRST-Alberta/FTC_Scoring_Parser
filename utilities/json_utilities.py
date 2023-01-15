
from urllib.request import urlopen
import json
from pathlib import Path

def load_JSON_From_File(filepath: str) -> dict:
    filepath = Path(filepath)
    if not filepath.exists():
        print("file does not exist: {}".format(filepath))
        return {}
    with open(filepath, "r") as f:
        data = json.load(f)
    if not data:
        print("File was empty!")
        return {}
    else:
        return data

def load_JSON_From_URL(url: str) -> dict:
    response = urlopen(url)
    data = json.loads(response.read())
    if not data:
        print("Response from URL was empty! {}".format(url))
        return {}
    else:
        return data