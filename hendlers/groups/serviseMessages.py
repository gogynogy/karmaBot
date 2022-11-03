from aiogram import types
from aiogram.dispatcher.filters import IsReplyFilter

from loader import dp

@dp.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def welcome_message(message: types.Message):
    members = ", ".join([mess.get_mention(as_html=True) for mess in message.new_chat_members])
    await message.reply(f"привет {members} 🤚")

@dp.message_handler(content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def buye_message(message: types.Message):
    if message.left_chat_member == message.from_user.id:
        await message.reply(f"👤 {message.left_chat_member.get_mention(as_html=True)} вышел из чата")
    else:
        await message.reply(f"👤 {message.left_chat_member.get_mention(as_html=True)} удален из чата"
                            f" пользователем {message.from_user.get_mention(as_html=True)}")


@dp.message_handler(content_types=types.ContentType.ANY)
async def changing_karma_sticker(message: types.Message):
    await message.reply("emodzy")