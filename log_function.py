from log_settings import logger


def log_registration(username):
    """Логирование регистрации пользователя"""
    logger.info(f'Пользователь {username} зарегистрировался')

