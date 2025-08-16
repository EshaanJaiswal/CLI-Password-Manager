import json
try:
    from .constants import DATA
except ImportError:
    from constants import DATA


class DBM:
    def load_db(self):
        try:
            with open(DATA, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            print("Database file is corrupted. Starting with an empty database. (JSON Decode Error)")
            return {}
    
    def save_db(self, data: dict):
        with open(DATA, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, sort_keys=True)
