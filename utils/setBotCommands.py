from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        # types.BotCommand('start', 'Запустить бот'),
        # types.BotCommand('help', 'Помощь'),
        types.BotCommand('beer', 'хочу пива')
    ])