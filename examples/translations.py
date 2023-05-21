from aiogram_translation.models import BaseTranslationBuilder


class BaseTranslation(BaseTranslationBuilder):
    start_message: str
    start_button: str
    start_button_alert: str


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
    key = "uk"
    name = "Український (Ukrainian)"

    start_message = "👋 Привіт, я бот"
    start_button = "❤️ Натисни на мене"
    start_button_alert = "🎉 Ура!"