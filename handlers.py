from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command

from database.db import SessionLocal
from database.models import User, MessageLog
from log_function import log_registration, log_about_my_history, log_about_user_info

router = Router()


@router.message(CommandStart())
async def start_handler(message: types.Message):
    """реагирует на команду /start"""
    session = SessionLocal()
    tg_id = message.from_user.id
    user = session.query(User).filter(User.telegram_id == tg_id).first()
    print(message.from_user)
    log_registration(username=message.from_user.username, user_id=tg_id)
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


@router.message(Command('myinfo'))
async def myinfo_handler(message: types.Message):
    session = SessionLocal()
    user = session.query(User).filter(User.telegram_id == message.from_user.id).first()
    first_name = message.from_user.first_name
    print("*" * 50, message.from_user)
    log_about_user_info(first_name=first_name,
                        username=message.from_user.username,
                        user_id=message.from_user.id,
                        )
    if user:
        await message.answer(
            f"Ваш id: {user.telegram_id}\n"
            f"Ваш никнейм: {user.username}\n"
            f"Регистрация: {user.registered_at}\n"
        )
    else:
        await message.answer('Нет регистрации')
    session.close()


@router.message(Command('history'))
async def history_handler(message: types.Message):
    session = SessionLocal()
    user = session.query(User).filter(User.telegram_id == message.from_user.id).first()
    log_about_my_history(username=message.from_user.username, user_id=message.from_user.id)

    if user:
        messages = (session.query(MessageLog).
                    filter(MessageLog.user_id == user.id).
                    order_by(MessageLog.timestamp.desc()).
                    limit(3).
                    all())
        if messages:
            text = "\n".join([f"{m.timestamp}: {m.message_text}" for m in messages])
            await message.answer(f'Последние сообщения:\n{text}')

    session.close()


@router.message(F.text.regexp(r"^(?!\/).+"))
async def log_message(message: types.Message):
    session = SessionLocal()
    user = session.query(User).filter(User.telegram_id == message.from_user.id).first()

    if user:
        log = MessageLog(user_id=user.id, message_text=message.text)
        session.add(log)
        session.commit()

    session.close()
