from aiogram import types
from SQLBD import SQL
from data.dict import good_words, bad_words
from loader import dp
from utils.notify_admins import write_admin

SQL = SQL()


# @dp.message_handler()
# async def check_message(message: types.Message):
#     text = message.text.lower().split(' ')
#     try:
#         for letter in text:
#             if letter in good_words:
#                 await message.answer(f"+ {letter}")
#                 SQL.change_karma("plus", message.chat.id)
#             elif letter in bad_words:
#                 await message.answer(f"- {letter}")
#                 SQL.change_karma("plus", message.chat.id)
#     except:
#         await write_admin(f"Ошибка при работе check_message")
