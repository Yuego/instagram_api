
from instagram_api.instagram_base import InstagramInterface

class RequestBase:

    ig: InstagramInterface

    def __init__(self, ig: InstagramInterface):
        self.ig = ig
