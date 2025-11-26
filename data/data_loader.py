class DataLoader:
    def __init__(self):
        pass

    def load_json(self, path):
        import json
        try:
            with open(path, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading JSON: {e}")
            return None
