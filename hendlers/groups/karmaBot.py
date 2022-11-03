from aiogram import types
from SQLBD import SQL
from data.dict import good_words
from loader import dp

@dp.message_handler()
async def check_message(message: types.Message):
    text = message.text.lower().split(' ')
    for letter in text:
        if letter in good_words:
            await message.answer(f"letter")
            # SQL.change_karma("plus", message.chat.id)



