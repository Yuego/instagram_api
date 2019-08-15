from typing import Union
from urllib.request import BaseHandler, HTTPCookieProcessor


class FakeCookiesHandler(HTTPCookieProcessor):

    pass

