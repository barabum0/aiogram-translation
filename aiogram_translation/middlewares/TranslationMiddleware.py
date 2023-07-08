from typing import Callable, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message, Update


class TranslationMiddleware(BaseMiddleware):
    def __init__(self, translator: "Translator", key: str = "language") -> None:
        self._translator = translator
        self._key = key

    async def __call__(
        self,
        handler: Callable[[Update, dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: dict[str, Any]
    ) -> Any:
        update = event.callback_query or event.message or event.channel_post\
                or event.chat_member or event.edited_message or event.chat_join_request\
                or event.chosen_inline_result or event.edited_channel_post\
                or event.my_chat_member or event.poll_answer.user or event.shipping_query\
                or event.pre_checkout_query
        user = update.from_user
        if user:
            code = user.language_code
        else:
            code = self._translator.get_default_key()
        data[self._key] = self._translator.get_translation(code)
        return await handler(event, data)