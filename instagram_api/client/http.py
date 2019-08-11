import pickle
import threading
from http.cookiejar import Cookie, CookieJar, CookiePolicy
from typing import Union


class ClientCookieJar(CookieJar):

    def __init__(self, cookie_string: Union[str, bytes] = None, policy: CookiePolicy = None):
        super(ClientCookieJar, self).__init__(policy=policy)

        if cookie_string:
            if isinstance(cookie_string, bytes):
                self._cookies = pickle.loads(cookie_string)
            else:
                self._cookies = pickle.loads(cookie_string.encode('utf-8'))

    @property
    def auth_expires(self):
        for cookie in self:
            if cookie.name in ('ds_user_id', 'ds_user'):
                return cookie.expires

        return None

    def __getstate__(self):
        state = self.__dict__.copy()

        del state['_cookies_lock']

        return state

    def __setstate__(self, state):
        self.__dict__.update(state)

        self._cookis_lock = threading.RLock()
