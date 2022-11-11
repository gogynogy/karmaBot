from aiogram.utils import executor

from hendlers import dp
from utils.notify_admins import on_start_up_notify
from utils.setBotCommands import set_default_commands

from SQLBD import SQL
SQL = SQL()

async def on_startup(dp):
    await on_start_up_notify()
    await set_default_commands(dp)
    print("бот запущен")
    SQL.checkDB()


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, on_startup=on_startup, skip_updates=True)
