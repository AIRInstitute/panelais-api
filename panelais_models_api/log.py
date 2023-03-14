#!/usr/bin/python3
# Copyright 2023 BISITE
# See LICENSE for details.
# Author: Francisco Pinto-Santos (@GandalFran on GitHub)


import logging
import logging.config
from typing import Any

LOGGER_NAME = 'panelais-models-api'
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'loggers': {
        '': {
            'level': 'ERROR',
            'handlers': ['consoleHandler']
        },
        LOGGER_NAME: {
            'level': 'DEBUG',
            'propagate': False,
            'handlers': ['consoleHandler']
        }
    },
    'formatters': {
        'consoleFormatter': {
            'format': '[%(asctime)s][%(levelname)s][%(module)s][%(funcName)s] %(message)s'
        }
    },
    'handlers': {
        'consoleHandler': {
            'level': 'DEBUG',
            'formatter': 'consoleFormatter',
            'class': 'logging.StreamHandler'
        }
    }
}

logger = None
has_setup = False


def setup_logger() -> None:
    """Setups logger for cookiecutter.application_
    """

    global logger
    logging.config.dictConfig(LOGGING_CONFIG)
    logger = logging.getLogger(LOGGER_NAME)


def serve_application_logger() -> Any:
    """Setups logger for application if not initializes, and servers the application logger.

    Returns:
        :obj:`logging.logger` application logger
    """

    global has_setup, logger
    if not has_setup:
        setup_logger()
        has_setup = True
    return logger
