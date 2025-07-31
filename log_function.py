from log_settings import logger


def log_registration(username, user_id):
    """Логирование регистрации пользователя"""
    logger.info(f'Пользователь {username} (ID: {user_id}) зарегистрировался')


