import logging

"""Create a class for logging"""
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler('logs/root.log', 'w')
formatter = logging.Formatter('%(levelname)s:%(asctime)s:-%(name)s:->%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info('Welcome to logging !!!!')