from typing import TypeVar

from instagram_api.interfaces.api_response import ApiResponseInterface

T = TypeVar('T', bound=ApiResponseInterface)


class InstagramException(Exception):

    _response: T

    def __init__(self, *args, response: T = None, **kwargs):
        self.message = args[0]
        self._response = response

        super(InstagramException, self).__init__(*args, **kwargs)

    @property
    def has_response(self) -> bool:
        return self._response is not None

    @property
    def response(self) -> T:
        return self._response
