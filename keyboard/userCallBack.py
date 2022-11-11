from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData




cb_beer = CallbackData('w', 'id', 'what', 'count')

def buy_something(id, what, count):
    """Creates a button with the record id"""
    return InlineKeyboardButton(f'{what,} {count}', callback_data=cb_beer.new
        (id=id, what=what, count=count))

