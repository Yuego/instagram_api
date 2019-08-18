from instagram_api import response

from .base import CollectionBase

__all__ = ['Push']


class Push(CollectionBase):

    def register(self, push_channel: str, token: str) -> response.PushRegisterResponse: ...

    def get_preferences(self) -> response.PushPreferencesResponse: ...

    def set_preferences(self, preferences: dict) -> response.PushPreferencesResponse: ...
