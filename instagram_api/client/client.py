import pickle
import requests

from datetime import datetime

from http.cookiejar import Cookie, CookieJar
from http import cookies, client
from urllib import request, error, parse
from urllib.parse import urlparse

from typing import Optional

from instagram_api.instagram_base import InstagramInterface

from .fake_cookies import FakeCookiesHandler
from .zero_rating import ZeroRatingHandler


class Client:

    COOKIE_AUTOSAVE_INTERVAL = 45

    _ig: InstagramInterface

    _user_agent: str
    _verify_ssl: bool

    _proxy: Optional[str, dict]

    # output_interface: Optional[str]

    # client: None

    # fake_cookies: FakeCookies

    # zero_rating: ZeroRating

    _cookie_jar: CookieJar
    _cookie_jar_last_saved: datetime

    reset_connection: bool

    def __init__(self, ig: InstagramInterface):
        self._ig = ig

        self._verify_ssl = True
        self._proxy = None

        self._opener = requests.Session()
        self._session.verify = self._verify_ssl
        self._session.max_redirects = 8

        self._reset_connection = False

        request.build_opener()


    def update_from_current_settings(self, reset_cookie_jar: bool = False):

        self._user_agent = self._ig.device.get_user_agent()
        self.load_cookie_jar(reset_cookie_jar=reset_cookie_jar)

        if self.token is None:
            self._ig.is_maybe_logged_in = False

        # TODO: реализовать
        # self.zero_rating.blah_blah_blah

    def load_cookie_jar(self, reset_cookie_jar: bool = False):
        self._cookie_jar = None

        if reset_cookie_jar:
            self._ig.settings.set_cookies('')


