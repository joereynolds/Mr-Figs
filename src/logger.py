"""
The singleton logger to log all things fig related.
"""

import logging

LOGGER = logging.getLogger('mr-figs')
HANDLER = logging.FileHandler('mr-figs-log.log')
FORMATTER = logging.Formatter('%(asctime)s %(filename)s %(funcName)s %(levelname)s:%(lineno)d %(message)s')
HANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(HANDLER)
LOGGER.setLevel(logging.DEBUG)
