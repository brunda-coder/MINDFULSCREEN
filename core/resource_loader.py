import json
import os

class ResourceLoader:
    @staticmethod
    def load_json(path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"JSON file missing: {path}")
        with open(path, "r") as f:
            return json.load(f)
