from typing import Callable, Any, Awaitable

from aiogram import BaseMiddleware, Bot
from aiogram.types import Message, Update, User


class TranslationMiddleware(BaseMiddleware):
    def __init__(self, translator: "Translator", extract_language_function: Callable[[User, Bot], Awaitable[str]], key: str = "language") -> None:
        self._translator = translator
        self._key = key
        self.extract_language_function = extract_language_function

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
            code = await self.extract_language_function(user, data["bot"])
        else:
            code = self._translator.get_default_key()
        data[self._key] = self._translator.get_translation(code)
        return await handler(event, data)