import logging

from aiogram import Dispatcher

from data.config import admins

async def on_start_up_notify(dp: Dispatcher):
    for admin in admins:
        try:
            await dp.bot.send_message(admin, "бот запущен")
        except Exception as ex:
            logging.exception(ex)