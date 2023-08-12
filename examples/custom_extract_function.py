from aiogram import Dispatcher, Bot, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, User

from aiogram_translation import Translator
from translations import *

from os import getenv


async def force_russian_language(user: User, bot: Bot) -> str:
    force_list = [733876760]
    if user.id in force_list:
        return "uk"  # Set force ukrainian language for account with 733876760 id
    else:
        return user.language_code


bot = Bot(getenv("TELEGRAM_TOKEN"))
dispatcher = Dispatcher()
translator = Translator(extract_language_function=force_russian_language)

translator.include([
    English(),
    Russian(),
    Ukrainian()
])
translator.set_default('ru')
translator.register(dispatcher)


@dispatcher.message()
async def on_message(message: Message, language: BaseTranslation):
    kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=language.start_button,
                                                                     callback_data="hoooray")]])
    await message.reply(language.start_message, reply_markup=kb)


@dispatcher.callback_query(F.data == "hoooray")
async def on_hooray(query: CallbackQuery, language: BaseTranslation):
    await query.answer(language.start_button_alert, show_alert=True)


dispatcher.run_polling(bot)