#!/usr/bin/python3

import logging
import logging.handlers

logger = logging.getLogger('test')
logger.setLevel(logging.DEBUG)

handler = logging.handlers.RotatingFileHandler('test.log', maxBytes = 1024 * 1024, backupCount = 5)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
