from log_settings import logger


def log_registration(username, user_id):
    """Логирование регистрации пользователя"""
    logger.info(f'Пользователь {username} (ID: {user_id}) зарегистрировался')


def log_user_delete(username, user_id):
    """Логирование удаления пользователя"""
    logger.info(f'Пользователь {username} (ID: {user_id}) был удалён')


def log_about_my_history(username, user_id):
    """Логирование просмотра истории сообщений"""
    logger.info(f'Пользователь {username} (ID: {user_id}) просмотрел историю сообщений')


def log_about_user_info(username, first_name, user_id):
    """Логирование просмотра информации о пользователе"""
    logger.info(f'Пользователь с ником {username}, по имени {first_name}, (ID: {user_id}) просмотрел информацию о пользователе')
