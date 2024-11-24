import os
import requests
import zipfile
from io import BytesIO

def download_dataset():
    url = "https://www.dropbox.com/scl/fi/ti8m8az27cjvxefllv8ds/cherry-leaves.zip?rlkey=uj8hynh0js31fz9t5sknhss1o&dl=1"
    
    print("Downloading dataset...")
    response = requests.get(url)
    
    print("Extracting files...")
    with zipfile.ZipFile(BytesIO(response.content)) as zip_ref:
        zip_ref.extractall('data/cherry_leaves')
    
    print("Done!")

if __name__ == "__main__":
    os.makedirs('data/cherry_leaves', exist_ok=True)
    download_dataset()