from typing import Union, Callable, Awaitable

from aiogram import Dispatcher
from aiogram.types import User

from aiogram_translation.middlewares import TranslationMiddleware
from aiogram_translation.models import BaseTranslationBuilder
from aiogram_translation.errors import InvalidTranslation, InvalidDefaultTranslation


async def extract_language_from_user(user: User) -> str:
    return user.language_code


class Translator:
    def __init__(self,
                 default_language_key: str = None,
                 translations: list[BaseTranslationBuilder] = None,
                 extract_language_function: Callable[[User], Awaitable[str]] = extract_language_from_user):
        self._default_language_key = default_language_key
        self._translations = {}
        self.extract_language_function = extract_language_function
        if translations:
            self.include(translations)

    def include(self, translations: Union[BaseTranslationBuilder, list[BaseTranslationBuilder]]):
        if isinstance(translations, list):
            for translation in translations:
                self._translations[translation.linked_to_key or translation.key] = translation
        else:
            self._translations[translations.linked_to_key or translations.key] = translations

    def exclude(self, key: str):
        self._translations.pop(key)

    def set_default(self, key: str | None):
        self._default_language_key = key

    def get_translation(self, language_key: str) -> BaseTranslationBuilder:
        _translation = self._translations.get(language_key, None)
        if not _translation:
            if self._default_language_key:
                _translation = self._translations.get(self.get_default_key(), None)
                _translation.linked_to_key = language_key
            else:
                raise InvalidTranslation(
                    f'There is no translation with key \"{language_key}\" and default translation is not set.')
        return _translation

    def get_default_key(self):
        _translation = self._translations.get(self._default_language_key, None)
        if not _translation:
            raise InvalidDefaultTranslation(
                f'There is no translation with key \"{self._default_language_key}\" that is set by default.')
        return self._default_language_key

    def register(self, dp: Dispatcher, key: str = "language"):
        middleware = TranslationMiddleware(self, key=key, extract_language_function=self.extract_language_function)

        dp.update.middleware(middleware)
