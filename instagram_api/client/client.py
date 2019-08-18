from typing import Optional, Union

import json
import requests
import time

from time import time

from http.cookiejar import Cookie
from urllib.parse import urlparse

from instagram_api.constants import Constants
from instagram_api.exceptions import (
    BadRequestException,
    EmptyResponseException,
    InstagramException,
    LoginRequiredException,
    NetworkException,
    NotFoundException,
    RequestHeadersTooLargeException,
    ThrottledException,

)
from instagram_api.exceptions.server_message_raiser import ServerMessageRaiser
from instagram_api.interfaces.client import ClientInterface
from instagram_api.response.mapper.exceptions import PropertyMapperException
from instagram_api.response.mapper import ApiResponse
from instagram_api.response.direct_send_item import DirectSendItemResponse

from instagram_api.utils.http import (
    ClientCookieJar,
    create_cookie_jar_proxy,
    Session,
)
from .middleware import FakeCookiesMiddleware, ZeroRatingMiddleware, MiddlewareHTTPAdapter

__all__ = ['Client']


class Client(ClientInterface):
    COOKIE_AUTOSAVE_INTERVAL = 45

    _user_agent: str
    _verify_ssl: bool

    _proxy: Union[str, dict]

    _http_adapter: MiddlewareHTTPAdapter
    _fake_cookies: FakeCookiesMiddleware
    _zero_rating: ZeroRatingMiddleware

    _cookie_jar: ClientCookieJar
    _cookie_jar_last_saved: int

    _reset_connection: bool

    def __init__(self, ig, middlewares: list = None, proxy: Union[str, list, dict] = None):
        from instagram_api.instagram import Instagram
        self._ig: Instagram = ig

        middlewares = middlewares or []

        self._verify_ssl = True
        self._proxy = None

        self._session = Session()
        self._session.verify = self._verify_ssl
        self._session.max_redirects = 8

        self._fake_cookies = FakeCookiesMiddleware()
        self._zero_rating = ZeroRatingMiddleware()

        used_middlewares = [self._fake_cookies, self._zero_rating]
        used_middlewares.extend(middlewares)

        self._http_adapter = MiddlewareHTTPAdapter(used_middlewares)

        self._session.mount('http://', self._http_adapter)
        self._session.mount('https://', self._http_adapter)

        if proxy:
            self.set_proxy(proxy)
        else:
            self.clear_proxy()

        self._cookie_jar = ClientCookieJar()

        self._session.cookies = create_cookie_jar_proxy(self, '_cookie_jar')

        self._reset_connection = False

    def __call__(self, endpoint: str, headers: dict = None, data: dict = None, files: dict = None):
        if self._reset_connection:
            # Сбрасываем кеш соединений
            self._http_adapter.restart()
            self._reset_connection = False

        headers = headers or {}
        headers.update(self.force_headers)

        try:
            if not data and not files:
                response: requests.Response = self._session.get(endpoint, headers=headers)
            else:
                response: requests.Response = self._session.post(endpoint, data=data, files=files, headers=headers)
        except Exception as e:
            raise NetworkException(*e.args)

        http_code = response.status_code

        if http_code == 429:
            raise ThrottledException('Throttled by Instagram because of too many API requests.')
        elif http_code == 431:
            raise RequestHeadersTooLargeException('The request start-line and/or headers are too large to process.')

        if time() - self._cookie_jar_last_saved > self.COOKIE_AUTOSAVE_INTERVAL:
            self.save_cookie_jar()

        return response

    @property
    def force_headers(self):
        return {
            'User-Agent': self._user_agent,
            'Connection': 'Keep-Alive',
            'X-FB-HTTP-Engine': Constants.X_FB_HTTP_Engine,
            'Accept': '*/*',
            'Accept-Encoding': Constants.ACCEPT_ENCODING,
            'Accept-Language': Constants.ACCEPT_LANGUAGE,
        }

    @property
    def fake_cookies(self) -> FakeCookiesMiddleware:
        return self._fake_cookies

    @property
    def zero_rating(self) -> ZeroRatingMiddleware:
        return self._zero_rating

    def set_proxy(self, proxy: Union[str, list, dict]):
        if isinstance(proxy, str):
            parsed_url = urlparse(proxy)
            proxy_address = f'{parsed_url.scheme}://{parsed_url.netloc}'

            self._session.proxies.update({parsed_url.scheme: proxy_address})

        elif isinstance(proxy, (list, set, tuple)):
            for item in proxy:
                parsed_url = urlparse(item)
                proxy_address = f'{parsed_url.scheme}://{parsed_url.netloc}'

                self._session.proxies.update({parsed_url.scheme: proxy_address})

        elif isinstance(proxy, dict):
            for scheme, address in proxy.items():
                parsed_url = urlparse(address)
                proxy_address = f'{scheme}://{parsed_url.netloc}'

                self._session.proxies.update({scheme: proxy_address})

        else:
            raise ValueError('Unknown proxy type `{proxy}`')

        self._reset_connection = True

    def clear_proxy(self):
        self._session.proxies = {}
        self._reset_connection = True

    def update_from_current_settings(self, reset_cookie_jar: bool = False):

        self._user_agent = self._ig.device.user_agent

        self.load_cookie_jar(reset_cookie_jar)

        self._zero_rating.update(self._ig.settings.get_rewrite_rules())

    def load_cookie_jar(self, reset_cookie_jar: bool = False):
        self._cookie_jar = None

        if reset_cookie_jar:
            self._ig.settings.reset_cookies()

        self._cookie_jar = self._ig.settings.get_cookies()
        self._session.cookies = self._cookie_jar

        self._cookie_jar_last_saved = time()

    def save_cookie_jar(self):
        self._ig.settings.set_cookies(self._cookie_jar)

        self._cookie_jar_last_saved = time()

    def get_cookie(self, name: str, domain: str = None, path: str = None):
        now = int(time.time())
        future = now + 100 * 365 * 24 * 60 * 60

        if not domain:
            pass

        cookie: Cookie
        for cookie in sorted(self._cookie_jar, key=lambda c: c.expires or future, reverse=True):
            if cookie.expires and cookie.expires < now:
                continue

            if domain:
                cookie_domain: str = cookie.domain
                if cookie_domain.startswith('.'):
                    cookie_domain = cookie_domain[1:]

                if not domain.endswith(cookie_domain):
                    continue

            if path and cookie.path != path:
                continue

            if cookie.name.lower() == name.lower():
                return cookie.value

        return None

    def get_token(self):
        return self.get_cookie('csrftoken', domain='i.instagram.com')

    @staticmethod
    def api_body_decode(json_string: str) -> dict:
        return json.loads(json_string, strict=False)

    def map_server_response(self,
                            api_response: ApiResponse.__class__,
                            json_response: str,
                            http_response: requests.Response) -> ApiResponse:

        json_data = self.api_body_decode(json_response)

        if not isinstance(json_data, (dict, list, tuple, set)):
            status_code = http_response.status_code

            if status_code == 400:
                raise BadRequestException('Invalid request options.')
            elif status_code == 404:
                raise NotFoundException('Requested resource does not exist.')
            else:
                raise EmptyResponseException('No response from server. Either a connection or configuration error.')

        try:
            response = api_response(json_data)
        except PropertyMapperException as e:
            raise InstagramException(*e.args)

        response.http_response = http_response

        if not response:
            if isinstance(response, DirectSendItemResponse) and response.payload is not None:
                message = response.payload.get_message()
            else:
                message = response.get_message()

            try:
                ServerMessageRaiser.auto_raise(
                    response.__class__.__name__,
                    message,
                    response,
                    http_response,
                )
            except LoginRequiredException:
                self._ig.is_maybe_logged_in = False

                raise

        return response
