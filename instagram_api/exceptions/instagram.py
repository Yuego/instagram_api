from instagram_api.interfaces import ApiResponseInterface


class InstagramException(Exception):

    _response: ApiResponseInterface

    def __init__(self, *args, response: ApiResponseInterface = None, **kwargs):
        self.message = args[0]
        self._response = response

        super(InstagramException, self).__init__(*args, **kwargs)

    @property
    def has_response(self) -> bool:
        return self._response is not None

    @property
    def response(self) -> ApiResponseInterface:
        return self._response
