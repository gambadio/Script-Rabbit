# temp_data.py
import os
import json

TEMP_FILE = "last_batch.json"

def save_last_batch(folder_path):
    try:
        with open(TEMP_FILE, 'w') as f:
            json.dump({"last_batch": folder_path}, f)
    except Exception as e:
        print(f"Error saving last batch info: {e}")

def get_last_batch():
    try:
        if os.path.exists(TEMP_FILE):
            with open(TEMP_FILE, 'r') as f:
                data = json.load(f)
                return data.get("last_batch")
    except Exception as e:
        print(f"Error reading last batch info: {e}")
    return None

def clear_temp_data():
    try:
        if os.path.exists(TEMP_FILE):
            os.remove(TEMP_FILE)
    except Exception as e:
        print(f"Error clearing temp data: {e}")
