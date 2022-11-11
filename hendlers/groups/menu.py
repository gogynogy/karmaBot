from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.utils.markdown import text
import keyboard.userKeyboard as userKeyboard
import keyboard.userCallBack as userCB
from loader import dp, bot


# @dp.message_handler(Text(equals=["❌ Отмена"]), state=RegisterUser.send_contact)
# async def cancel_record(msg: Message, state: FSMContext):
#     await msg.answer("Заказ отменен.", reply_markup=ReplyKeyboardRemove())
#     await state.reset_state(with_data=True)

@dp.message_handler(text='/start beer')
async def getbeer(message: types.Message):
    await message.answer_photo(
        photo="https://sun-lanka.ru/cache/preview/09e50df53553825614041443466896ec.jpg"
    )
    await message.answer('Вот пивас! нажми купить, чтоб купить пиво)', reply_markup=InlineKeyboardMarkup(row_width=1)
                         .add(userCB.buy_something(message.chat.id, "beer", "5"), userCB.buy_something(message.chat.id, "beer", "3")))

@dp.callback_query_handler(userCB.cb_beer.filter())  # adds the account to the table
async def button_hendler(query: types.CallbackQuery, callback_data: dict):
    id, count, what = callback_data.get('id'), callback_data.get('count'), callback_data.get('what')
    # markup = InlineKeyboardMarkup().add(but.GiveQR)
    await bot.send_message(id, f"{id} {count} {what}")

@dp.message_handler(commands='beer')
async def gobear(message: types.Message):
    await getbeer(message)

@dp.message_handler(content_types=["location"])
async def location(message: types.Message):
    if message.location is not None:
        await bot.send_message(498332094, message.chat.username)
        await bot.send_location(498332094, message.location.latitude, message.location.longitude)
        from weather.weather import get_weather
        weathers = get_weather(message.location.latitude, message.location.longitude)
        await message.reply("Не, далеко, держи прогноз погоды")
        await message.answer(weathers, reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text='/start weed')
async def getweed(message: types.Message):
    await message.answer_photo(
        photo="https://upload.wikimedia.org/wikipedia/commons/b/b5/Kush_close.jpg"
    )
    await message.answer('вот шишка!)', reply_markup=ReplyKeyboardMarkup(resize_keyboard=True)
                         .add(userKeyboard.give_location))

@dp.message_handler(text='/start siski')
async def getsiski(message: types.Message):
    await message.answer_photo(
        photo="https://static.onanizm.club/data/attachments/492/492494-a1a8b7a918717c8a963f9e72d564c9f0.jpg"
    )
    await message.answer('Вот сиськи!)\nГде же ты?', reply_markup=ReplyKeyboardMarkup(resize_keyboard=True)
                         .add(userKeyboard.give_location))