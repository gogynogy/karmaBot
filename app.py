from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, message
from aiogram.utils import executor
from SQLBD import SQL
from config import BOT_TOKEN, good_words
# from utils.nick import rate_limit



bot = Bot(token=BOT_TOKEN)

dp = Dispatcher(bot, storage=MemoryStorage())



@dp.message_handler()
async def get_message(message: types.Message):
    print(len(message.text))
    message_split = message.text.split(" ")
    for i in message_split:
        if i.startswith("@"):
            await bot.send_message(message.chat.id, i)
        elif i in good_words:
            await bot.send_message(message.chat.id, i)



if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)