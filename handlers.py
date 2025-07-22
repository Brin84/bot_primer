from aiogram import Router, types
from aiogram.filters import CommandStart

from database.db import SessionLocal
from database.models import User

router = Router()

@router.message(CommandStart)
async def start_handler(message: types.Message):
    """реагирует на команду /start"""
    session = SessionLocal()
    tg_id = message.from_user.id
    user = session.query(User).filter(User.telegram_id == tg_id).first()
    if not user:
        user = User(
            telegram_id=tg_id,
            username=message.from_user.username,
            first_name=message.from_user.first_name
        )
        session.add(user)
        session.commit()
        await message.answer('Вы зарегистрированы')
    else:
        await message.answer('Вы уже зарегистрированы')
    session.close()