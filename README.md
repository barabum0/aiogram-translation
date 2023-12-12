<div align="center">

# Aiogram Translation Plugin 🌐

[![Supported Python versions](https://img.shields.io/pypi/pyversions/aiogram-translation.svg?style=flat-square&logo=python&logoColor=FFE873)](https://pypi.org/project/aiogram-translation)
![aiogram v3.0.0b7](https://img.shields.io/badge/aiogram-v3.0.0b7+-green?style=flat-square&logo=telegram)
[![PyPI version](https://img.shields.io/pypi/v/aiogram-translation.svg?style=flat-square&logo=pypi&logoColor=FFE873)](https://pypi.org/project/aiogram-translation)
[![PyPI downloads](https://img.shields.io/pypi/dm/aiogram-translation.svg?style=flat-square)](https://pypi.org/project/aiogram-translation)
[![wakatime](https://wakatime.com/badge/github/barabum0/aiogram-translation.svg)](https://wakatime.com/badge/github/barabum0/aiogram-translation)

</div>

## About 📘

The Aiogram Translation Plugin is a convenient and powerful tool for integrating multilingual support into Aiogram-based Telegram bots. It enables seamless translation and language handling, making your bot accessible to a wider, global audience.

## Installation 📥

```shell
python -m pip install -U aiogram-translation 
```

## Usage 🛠️

To use the Aiogram Translation Plugin in your bot, import the necessary classes from `aiogram_translation`. Set up your languages, default language, and register the translator with your dispatcher. Here's a basic example:

`main.py` 
```python
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
    Russian(),
    Ukrainian()
])
translator.set_default('ru')
translator.register(dispatcher)


@dispatcher.message()
async def on_message(message: Message, language: BaseTranslation):
    kb = InlineKeyboardMarkup(resize_keyboard=True, inline_keyboard=[[InlineKeyboardButton(text=language.start_button,
                                                                                           callback_data="hoooray")]])
    await message.reply(language.start_message, reply_markup=kb)


@dispatcher.callback_query(F.data == "hoooray")
async def on_hooray(query: CallbackQuery, language: BaseTranslation):
    await query.answer(language.start_button_alert, show_alert=True)


dispatcher.run_polling(bot)
```

`translations.py`
```python
from aiogram_translation.models import BaseTranslationBuilder


class BaseTranslation(BaseTranslationBuilder):
    start_message: str
    start_button: str
    start_button_alert: str

    link_lang_message: str


class English(BaseTranslation):
    key = "en"
    name = "English"

    start_message = "👋 Hi, I'm bot!"
    start_button = "❤️ Click me!"
    start_button_alert = "🎉 Hooray!"


class Russian(BaseTranslation):
    key = "ru"
    name = "Русский (Russian)"

    start_message = "👋 Привет, я бот"
    start_button = "❤️ Нажми на меня"
    start_button_alert = "🎉 Ура!"


class Ukrainian(BaseTranslation):
    # Was translated from Russian with Yandex Translate, so sorry if it got wrong
    key = "uk"
    name = "Український (Ukrainian)"

    start_message = "👋 Привіт, я бот"
    start_button = "❤️ Натисни на мене"
    start_button_alert = "🎉 Ура!"
```


## Troubleshooting 🚨

If you encounter issues or have queries, feel free to check our [Issues section](https://github.com/barabum0/aiogram-translation/issues) on GitHub.

## Contribution 🤝

Contributions are welcome. Please fork the repository, make your changes, and submit a pull request.

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.