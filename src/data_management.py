import pickle


def load_pkl_file(file_path):
    """
    Load pickle file.

    Args:
        file_path: Path to the pickle file
        
    Returns:
        Data from pickle file
    """
    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
        return data
    except Exception as e:
        print(f"Error loading pickle file: {e}")
        return None


def save_pkl_file(data, file_path):
    """
    Save data to pickle file.
    
    Args:
        data: Data to save
        file_path: Path where to save the file

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(file_path, 'wb') as file:
            pickle.dump(data, file)
        return True
    except Exception as e:
        print(f"Error saving pickle file: {e}")
        return False
