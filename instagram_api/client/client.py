from datetime import datetime

from http.cookiejar import Cookie, CookieJar

from typing import Optional

from instagram_api.instagram_base import InstagramInterface


class Client:

    COOKIE_AUTOSAVE_INTERVAL = 45

    ig: InstagramInterface

    user_agent: str
    verify_ssl: bool

    proxy: Optional[str, dict]

    output_interface: Optional[str]

    client: None

    fake_cookies: FakeCookies

    zero_rating: ZeroRating

    cookie_jar: CookieJar
    cookie_jar_last_saved: datetime

    reset_connection: bool

    def __init__(self, ig: InstagramInterface):
        self.ig = ig

        self.verify_ssl = True
        self.proxy = None

