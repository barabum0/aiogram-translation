from pydantic import BaseModel


class BaseTranslationBuilder(BaseModel):
    key: str
    name: str