import logging
import os
from datetime import datetime


def setup_logger(name='mildew_detector'):
    """Configure and set up logging system."""
    log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)

    log_filename = (
        f'mildew_detection_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
    )
    log_filepath = os.path.join(log_dir, log_filename)

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_filepath),
            logging.StreamHandler()
        ]
    )

    return logging.getLogger(name)


logger = setup_logger()
