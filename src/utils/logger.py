import logging
import os
from datetime import datetime


class Logger:
    """Custom logger class."""

    def __init__(self, name, log_dir='logs'):
        """Initialize logger with name and directory."""
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        # Create logs directory if it doesn't exist
        os.makedirs(log_dir, exist_ok=True)

        # Create file handler
        log_file = os.path.join(
            log_dir,
            f'{name}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
        )
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)

        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def info(self, message):
        """Log info message."""
        self.logger.info(message)

    def error(self, message):
        """Log error message."""
        self.logger.error(message)

    def warning(self, message):
        """Log warning message."""
        self.logger.warning(message)


logger = Logger('mildew_detection')
