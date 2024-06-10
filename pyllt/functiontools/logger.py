import datetime
import logging
import os

import numpy as np

__all__ = ['Logger']


def ensure_directory_exists(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directory '{directory_path}' created.")
    else:
        print(f"Directory '{directory_path}' already exists.")


class ColoredFormatter(logging.Formatter):
    # Define the color codes
    COLORS = {
        'reset': '\033[0m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'red': '\033[91m',
        'cyan': '\033[96m',
        'blue': '\033[94m',
        'white': '\033[97m',
        'grey': '\033[90m'
    }

    def format(self, record):
        # Ensure that the asctime is included in the record
        if self.usesTime():
            record.asctime = self.formatTime(record, self.datefmt)

        # Apply colors to each part of the log message
        log_message = (
            f"{self.COLORS['green']}{record.asctime}{self.COLORS['reset']} - "
            f"{self.COLORS['yellow']}{record.name}{self.COLORS['reset']} - "
            f"{self.COLORS['red']}{record.levelname}{self.COLORS['reset']} - "
            f"{self.COLORS['cyan']}{record.getMessage()}{self.COLORS['reset']} - "
            f"{self.COLORS['blue']}{record.pathname}{self.COLORS['reset']} - "
            f"{self.COLORS['white']}{record.lineno}{self.COLORS['reset']} - "
            f"{self.COLORS['grey']}{record.funcName}{self.COLORS['reset']}"
        )
        return log_message


class Logger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        ensure_directory_exists('./logs')
        file_handler = logging.FileHandler(f'./logs/full_info_{np.random.randint(0, 99)}_{datetime.datetime.now()}.log')

        console_handler.setLevel(logging.DEBUG)
        file_handler.setLevel(logging.DEBUG)

        color_formatter = ColoredFormatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(pathname)s - %(lineno)d - %(funcName)s'
        )
        plain_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(pathname)s - %(lineno)d - %(funcName)s'
        )

        console_handler.setFormatter(color_formatter)
        file_handler.setFormatter(plain_formatter)

        # Add the handlers to the logger
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

    def log(self, message, level=None):
        if level is None:
            level = 'default'

        if level == 'debug':
            self.logger.debug(message)
        elif level == 'info':
            self.logger.info(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        elif level == 'critical':
            self.logger.critical(message)
        elif level == 'exception':
            self.logger.exception(message)
        else:
            self.logger.log(level=0, msg=message)
