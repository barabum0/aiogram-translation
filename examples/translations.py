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

    link_lang_message = "This must be {orig_lang} language, but it become {linked_lang} language 🤷"


class Russian(BaseTranslation):
    key = "ru"
    name = "Русский (Russian)"

    start_message = "👋 Привет, я бот"
    start_button = "❤️ Нажми на меня"
    start_button_alert = "🎉 Ура!"

    link_lang_message = "Это должен был быть {orig_lang} язык, но он превратился в {linked_lang} язык 🤷"


class Ukrainian(BaseTranslation):
    # Was translated from Russian with Yandex Translator, so sorry if it got wrong
    key = "uk"
    name = "Український (Ukrainian)"

    start_message = "👋 Привіт, я бот"
    start_button = "❤️ Натисни на мене"
    start_button_alert = "🎉 Ура!"

    link_lang_message = "Це мало бути {orig_lang} мова, але вона перетворилася на {linked_lang} мова 🤷"