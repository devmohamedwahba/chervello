"""This Module To Implement Logger File."""

import logging
import sys
import os
from datetime import datetime
from utils import BASE_DIR
from utils.singleton import SingletonMeta

LOG_DIRECTORY = os.path.join(BASE_DIR, "logs")
UNIQ_NAME = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}"
LOG_FILE_NAME = os.path.join(LOG_DIRECTORY, "logs_" + UNIQ_NAME + ".log")


def _initialize_log_directory():
    """Creates the log directory and all intermediate directories if not already existing."""
    if not os.path.exists(LOG_DIRECTORY):
        os.makedirs(LOG_DIRECTORY)


class LogHandler(metaclass=SingletonMeta):
    def __init__(self):
        self.logger = logging.getLogger("VOTA")
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)
            formatter = logging.Formatter(
                "%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s", datefmt="%d-%m-%Y %H:%M:%S"
            )
            _initialize_log_directory()

            self.file_handler = logging.FileHandler(LOG_FILE_NAME)
            self.file_handler.setFormatter(formatter)
            self.logger.addHandler(self.file_handler)

            self.stream_handler = logging.StreamHandler(sys.stdout)
            self.stream_handler.setFormatter(formatter)
            self.logger.addHandler(self.stream_handler)

            self.logger.info(f"Initiating {type(self).__name__} ...")
