import re

from .base import BaseMiddleware

__all__ = ['ZeroRatingMiddleware']


class ZeroRatingMiddleware(BaseMiddleware):
    ordering = 115

    DEFAULT_REWRITE = {
        r'^(https?:\/\/)(i)(\.instagram\.com/.*)$': '\\1b.\\2\\3',
    }

    _rules: dict

    def __init__(self):
        self._rules = {}
        self.reset()

    def reset(self):
        self.update(self.DEFAULT_REWRITE)

    def update(self, rules: dict):
        for pattern, repl in rules.items():

            try:
                re.match(pattern, '')
            except re.error:
                continue

            self._rules[pattern] = repl.replace('\\.', '.')

    def rewrite(self, uri: str) -> str:
        for pattern, repl in self._rules:
            result = re.sub(pattern, repl, uri)
            if not result:
                continue

            if result != uri:
                return result

        return uri

