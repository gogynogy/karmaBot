from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, message
from aiogram.utils import executor
from SQLBD import SQL
from config import BOT_TOKEN, good_words
# from utils.nick import rate_limit

BD = SQL()
BD.checkDB()

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=["start"])  # /start command processing
async def begin(message: types.Message):
    markup = InlineKeyboardMarkup(row_width=1)
    await bot.send_message(message.chat.id, "привет")

# @dp.message_handler(content_types=types.ContentType.ANY)
# async def take_message(message: types.Message):
#     print(len(message.text))
#     message_split = message.text.split(" ")
#     for i in message_split:
#         if i.startswith("@"):
#             await bot.send_message(message.chat.id, i)
#         elif i in good_words:
#             await bot.send_message(message.chat.id, i)

@dp.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def welcome_message(message: types.Message):
    members = ", ".join([mess.get_mention(as_html=True) for mess in message.new_chat_members])
    await message.reply(f"привет {members}")
    print(message.new_chat_members)
    print(members)



if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)