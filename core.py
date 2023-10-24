import logging

"""Create a class for logging"""
formatter = logging.Formatter('%(levelname)s:%(asctime)s:-%(module)s:%(funcName)s:%(name)s:-> %(message)s')
# extra = {'user': 'Uzo'}

handler = logging.FileHandler('logs/root.log', 'w')
handler.setFormatter(formatter)

logger = logging.getLogger('CORElogger')
logger.setLevel(logging.INFO)

logger.addHandler(handler)

# logger.info('Welcome to logging !!!!')
    

if __name__ == '__main__':
    logger.info('This is the pytools project')


