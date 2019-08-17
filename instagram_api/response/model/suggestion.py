from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .user import User

__all__ = ['Suggestion', 'SuggestionInterface']


class SuggestionInterface(ApiInterfaceBase):
    media_infos: AnyType
    social_context: str
    algorithm: str
    thumbnail_urls: [str]
    value: float
    caption: AnyType
    user: User
    large_urls: [str]
    media_ids: AnyType
    icon: AnyType
    is_new_suggestion: bool
    uuid: str


class Suggestion(PropertyMapper, SuggestionInterface):
    pass
