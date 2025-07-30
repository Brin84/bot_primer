from loguru import logger
import os, sys


os.makedirs('logs', exist_ok=True)
logger.remove()

logger.add(
    sys.stdout,
    colorize=True,
    format='<blue>{time:YYYY-MM-DD HH:mm:ss}</blue> | <level>{level}</level> | <cyan>{message}</cyan>')

logger.add(
    'logs/my_log.log',
    rotation='3 MB',
    compression='zip',
    level='INFO',
    format= 'YYYY-MM-DD HH:mm:ss | {level} | {message}'
)