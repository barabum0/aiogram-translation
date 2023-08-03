from aiogram import Dispatcher, Bot, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from aiogram_translation import Translator
from translations import *

from os import getenv

bot = Bot(getenv("TELEGRAM_TOKEN"))
dispatcher = Dispatcher()
translator = Translator()

translator.include([
    English(),
    Ukrainian.link_to("ru"),  # Russian will become Ukrainian, instead of default English
    Ukrainian()
])
translator.set_default('en')
translator.register(dispatcher)


@dispatcher.message()
async def on_message(message: Message, language: BaseTranslation):
    await message.reply(language.link_lang_message.format(orig_lang=language.linked_to_key, linked_lang=language.key))


dispatcher.run_polling(bot)
