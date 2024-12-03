import logging
import os
from datetime import datetime

def setup_logger():
    """Configure logging system"""
    
    # Create logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')
        
    # Set up logging configuration
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            # File handler for persistent logs
            logging.FileHandler(
                f'logs/app_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
            ),
            # Stream handler for console output
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger(__name__)

logger = setup_logger()