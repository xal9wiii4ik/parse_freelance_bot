import logging

from aiogram import Dispatcher

from data.config import admins


async def on_startup_notify(dp: Dispatcher):

    for admin in admins:
        try:
            await dp.bot.send_message(chat_id=admin, text="Я Запущен)")
        except Exception as err:
            logging.exception(err)


async def on_shutdown_notify(dp: Dispatcher):

    for admin in admins:
        try:
            await dp.bot.send_message(chat_id=admin, text="Я все(")
        except Exception as err:
            logging.exception(err)
