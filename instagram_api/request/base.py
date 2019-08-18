
from instagram_api.interfaces import InstagramInterface


class CollectionBase:

    _ig: InstagramInterface

    def __init__(self, ig: InstagramInterface):
        self._ig = ig
