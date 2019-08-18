__all__ = ['CollectionBase']


class CollectionBase:

    def __init__(self, ig):
        from instagram_api.instagram import Instagram
        self._ig: Instagram = ig
