from typing import Any, Dict, Optional, Tuple

import random

from requests import Response
from urllib.parse import urlencode

from instagram_api.constants import Constants
from instagram_api.exceptions import LoginRequiredException
from instagram_api.interfaces.api_request import ApiRequestInterface
from instagram_api.signatures import Signatures
from instagram_api.utils import Utils

__all__ = ['ApiRequest']


class ApiRequest(ApiRequestInterface):

    _api_version: int = 1
    _url: str
    _params: dict
    _posts: dict
    _sign_exclude: list
    _body = None
    _files: dict
    _headers: dict
    _default_headers: bool

    _needs_auth: bool
    _sign_post: bool
    _sign_get: bool

    _is_multi_response: bool
    _is_body_compressed: bool

    _file_handlers = {}

    _response: Response

    def __init__(self, ig, url: str):
        from instagram_api.instagram import Instagram
        self._ig: Instagram = ig
        self._url = url

        self._api_version = 1
        self._headers = {}
        self._params = {}
        self._posts = {}
        self._files = {}
        self._file_handlers = {}
        self._needs_auth = True
        self._sign_post = True
        self._sign_get = False

        self._is_multi_response = False
        self._is_body_compressed = False

        self._sign_exclude = []
        self._default_headers = True

        self._response = None

    @property
    def default_headers(self):
        return {
            'X-IG-App-ID': Constants.FACEBOOK_ANALYTICS_APPLICATION_ID,
            'X-IG-Capabilities': Constants.X_IG_Capabilities,
            'X-IG-Connection-Type': Constants.X_IG_Connection_Type,
            'X-IG-Connection-Speed': '{0:d}kbps'.format(random.randint(1000, 3700)),
            'X-IG-Bandwidth-Speed-KBPS': '-1.000',
            'X-IG-Bandwidth-TotalBytes-B': '0',
            'X-IG-Bandwidth-TotalTime-MS': '0',
        }

    def _close_handlers(self):
        raise NotImplementedError

    def use_version(self, version: int):
        if version not in Constants.API_URLS:
            raise KeyError(f'`{version}` is not a supported API version.')

        self._api_version = Constants.API_URLS[version]

        return self

    def require_auth(self, flag: bool):
        self._needs_auth = flag

        return self

    def sign_get(self, flag: bool):
        self._sign_get = flag

        return self

    def sign_post(self, flag: bool):
        self._sign_post = flag

        return self

    def multi_json_response(self, flag: bool):
        self._is_multi_response = flag

        return self

    def compress_body(self, flag: bool):
        self._is_body_compressed = flag

        return self

    def use_default_headers(self, flag: bool):
        self._default_headers = flag

        return self

    def add_params(self, **params: Dict[str, Any]):
        for key, value in params.items():
            if value is True:
                value = 'true'
            elif value is False:
                value = 'false'

            self._params[key] = value

        return self

    def add_posts(self, **posts: Dict[str, Any]):
        for key, value in posts.items():
            if value is True:
                value = 'true'
            elif value is False:
                value = 'false'

            self._posts[key] = value

        return self

    def add_unsigned_posts(self, **posts):
        self.add_posts(**posts)
        self._sign_exclude.extend(posts.keys())

        return self

    def add_file(self, key: str, path: str, name: str, headers: Dict[str, str] = None):
        raise NotImplementedError

    def add_file_data(self, key: str, data: str, name: str, headers: dict = None):
        raise NotImplementedError

    def add_headers(self, **headers: Dict[str, str]):
        self._headers.update(headers)

    def get_http_response(self) -> Optional[Response]:
        if self._response is None:
            if self._needs_auth:
                self._raise_if_not_logged_in()

            self._reset_handlers()

            try:
                self._response = self._ig.client(*self._build_http_request())
            finally:
                self._close_handlers()

        return self._response

    def get_raw_response(self) -> str:
        http_response = self.get_http_response()

        body = http_response.text

        if self._is_multi_response:
            body = body.replace('}\r\n{', ',')

        return body

    def get_response(self, response_type):
        return self._ig.client.map_server_response(
            response_type,
            self.get_raw_response(),
            self.get_http_response(),
        )

    def _build_http_request(self) -> Tuple[str, dict, dict, dict]:
        endpoint = self._url
        if not (endpoint.startswith('http:') or endpoint.startswith('https:')):
            endpoint = ''.join([Constants.API_URLS[self._api_version], endpoint])

        if self._sign_get:
            self._params = Signatures.sign_data(self._params)

        if self._params:
            endpoint = ''.join([
                endpoint,
                '&' if '?' in endpoint else '?',
                urlencode(Utils.reorder_by_hash_code(self._params)),
            ])

        if self._default_headers:
            self.add_headers(**self.default_headers)

        if self._sign_post:
            self._posts = Signatures.sign_data(self._posts, self._sign_exclude)

        return endpoint, self._headers, self._posts, self._files

    def _raise_if_not_logged_in(self):
        if not self._ig.is_maybe_logged_in:
            raise LoginRequiredException('User not logged in. Please call login() and try again.')

    def _reset_handlers(self):
        self._file_handlers = {}
