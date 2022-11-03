from aiogram import types

from loader import dp


@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    print("1")
    await message.answer(f'hello {message.from_user.full_name}! \n'
                         f'your ID {message.from_user.id}')