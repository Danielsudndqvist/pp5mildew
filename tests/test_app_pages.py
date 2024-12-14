import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.app_pages.home import app

def test_home_app():
    """Test if home app function exists and is callable"""
    assert callable(app)
