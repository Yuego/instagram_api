
from instagram_api.interfaces.instagram import InstagramInterface


class Collection:

    ig: InstagramInterface

    def __init__(self, ig: InstagramInterface):
        self.ig = ig
