from typing import Optional

from pydantic import BaseModel


class BaseTranslationBuilder(BaseModel):
    key: str
    linked_to_key: Optional[str] = None
    name: str