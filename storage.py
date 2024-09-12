import json
import os

class Storage:
    DATA_DIR = "data"

    @staticmethod
    def ensure_data_dir():
        if not os.path.exists(Storage.DATA_DIR):
            os.makedirs(Storage.DATA_DIR)

    @staticmethod
    def get_file_path(filename):
        Storage.ensure_data_dir()
        return os.path.join(Storage.DATA_DIR, filename)

    @staticmethod
    def load_data(filename):
        file_path = Storage.get_file_path(filename)
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []
        return []

    @staticmethod
    def save_data(filename, data):
        """Save data to a file."""
        file_path = Storage.get_file_path(filename)
        with open(file_path, 'w') as file:
            if isinstance(data, list):
                json.dump([obj.__dict__ if hasattr(obj, '__dict__') else obj for obj in data], file, indent=4)
            else:
                json.dump(data, file, indent=4)
