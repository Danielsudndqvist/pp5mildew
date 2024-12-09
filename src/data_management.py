import pickle
import os

def load_pkl_file(file_path):
    """Load pickle file"""
    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
        return data
    except Exception as e:
        print(f"Error loading pickle file: {e}")
        return None

def save_pkl_file(data, file_path):
    """Save data to pickle file"""
    try:
        with open(file_path, 'wb') as file:
            pickle.dump(data, file)
        return True
    except Exception as e:
        print(f"Error saving pickle file: {e}")
        return False