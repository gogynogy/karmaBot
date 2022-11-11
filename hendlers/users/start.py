from aiogram import types, Dispatcher
from loader import bot

from loader import dp

@dp.message_handler(text='/start')
async def start(message: types.Message):
    await message.answer(f'hello {message.from_user.full_name}! \n'
                         f'your ID {message.from_user.id}')

@dp.callback_query_handler(lambda c: c.data == 'start')
async def startt(message: types.Message):
    await start(message)
def register_message_handler(dp: Dispatcher):
    dp.register_message_handler(start, text='/start')