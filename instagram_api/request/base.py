import random

from requests import Response

from instagram_api.constants import Constants
from instagram_api.interfaces import InstagramInterface, RequestInterface

__all__ = ['RequestBase']


class RequestBase(RequestInterface):
    _ig: InstagramInterface

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

    def __init__(self, ig: InstagramInterface, url: str):
        self._ig = ig
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

    def set_version(self, version: int):
        if version not in Constants.API_URLS:
            raise KeyError(f'`{version}` is not a supported API version.')

        self._api_version = Constants.API_URLS[version]

        return self

    def add_params(self, **params):
        for key, value in params.items():
            self._params[key] = 'true' if value else 'false'

        return self

    def get_http_response(self) -> Response:
        if self._response is None:
            if self._needs_auth:
                self._raise_if_not_logged_in()

            self._reset_handlers()

            try:
                self._response = self._ig.client()
            finally:
                self._close_handlers()

        return self._response

    def get_raw_response(self) -> str:
        http_response = self.get_http_response()


        return body

    def get_response(self, response_type):
        return self._ig.client.map_server_response(
            response_type,
            self.get_raw_response(),
            self.get_http_response(),
        )
