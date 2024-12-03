import numpy as np
import pandas as pd
from PIL import Image
import os
import base64
from datetime import datetime

def load_images_data():
    """
    Load and prepare image data from the dataset
    Returns two lists of image arrays: healthy and infected
    """
    healthy_path = "inputs/cherry-leaves/healthy"
    infected_path = "inputs/cherry-leaves/powdery_mildew"
    
    healthy_images = []
    infected_images = []
    
    # Load healthy images
    for image_file in os.listdir(healthy_path)[:10]:  # Limit for visualization
        if image_file.endswith(('.png', '.jpg', '.jpeg')):
            image = Image.open(os.path.join(healthy_path, image_file))
            healthy_images.append(image)
            
    # Load infected images
    for image_file in os.listdir(infected_path)[:10]:  # Limit for visualization
        if image_file.endswith(('.png', '.jpg', '.jpeg')):
            image = Image.open(os.path.join(infected_path, image_file))
            infected_images.append(image)
            
    return healthy_images, infected_images

def generate_features_analysis():
    """
    Generate summary statistics and analysis of the dataset
    """
    healthy_path = "inputs/cherry-leaves/healthy"
    infected_path = "inputs/cherry-leaves/powdery_mildew"
    
    healthy_count = len(os.listdir(healthy_path))
    infected_count = len(os.listdir(infected_path))
    
    analysis = {
        'total_images': healthy_count + infected_count,
        'healthy_count': healthy_count,
        'infected_count': infected_count,
        'distribution': {
            'healthy': healthy_count / (healthy_count + infected_count) * 100,
            'infected': infected_count / (healthy_count + infected_count) * 100
        }
    }
    
    return analysis

def download_dataframe_as_csv(df):
    """
    Generate a link allowing the data in a given pandas dataframe to be downloaded
    """
    datetime_now = datetime.now().strftime("%d%b%Y_%Hh%Mmin%Ss")
    csv = df.to_csv().encode()
    b64 = base64.b64encode(csv).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="Report_{datetime_now}.csv" target="_blank">Download Report</a>'
    return href