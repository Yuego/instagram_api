from typing import Union

from .base import BaseMiddleware

__all__ = ['FakeCookiesMiddleware']


class FakeCookiesMiddleware(BaseMiddleware):
    ordering = 100

    _cookies: dict

    def __init__(self):
        self.clear()

    def clear(self):
        self._cookies = {}

    def add(self, name: str, value: Union[str, int], single_use: bool = True, **kwargs):
        self._cookies[name] = {
            'value': value,
            'kwargs': kwargs,
            'single_use': single_use,
        }

    def delete(self, name: str):
        self._cookies.pop(name, None)

    def before_send(self, request, *args, **kwargs):
        print(dir(request))
        return None
