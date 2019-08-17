from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['CommentTranslations', 'CommentTranslationsInterface']


class CommentTranslationsInterface(ApiInterfaceBase):
    id: int
    translation: AnyType


class CommentTranslations(PropertyMapper, CommentTranslationsInterface):
    pass
