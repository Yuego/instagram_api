from requests import Response

from .interface_base import ApiInterfaceBase
from .mapper_base import PropertyMapperBase
from .mapper_meta import PropertyMapperMeta

from .error_list import ErrorList
from .message import Message

__all__ = ['ApiResponse', 'ApiResponseInterface']


class ApiResponseInterface(ApiInterfaceBase):
    status: str
    message: {str, ErrorList}
    error_type: str
    _messages: [Message]


class ApiResponse(PropertyMapperBase, ApiResponseInterface, metaclass=PropertyMapperMeta):
    STATUS_OK = 'ok'
    STATUS_FAIL = 'fail'

    _http_response: Response

    def __init__(self, data):
        super(ApiResponse, self).__init__(data)

        self._http_response = None

    def __bool__(self):
        return self.is_ok

    @property
    def is_ok(self):
        return self.status == self.STATUS_OK

    def _get_message(self, message):
        if message is None or isinstance(message, str):
            return message

        elif isinstance(message, dict):
            if 'errors' in message:
                errors = message['errors']
                if len(errors) > 1:
                    return f'Multiple Errors: %s.' % ' AND '.join(errors)
                else:
                    return errors[0]

            else:
                raise ValueError('Unknown message object. Expected errors subarray but found something else. '
                                 'Please submit a ticket about needing an instagram_api library update!')

        else:
            raise TypeError('Unknown message type. '
                            'Please submit a ticket about needing an instagram_api library update!')

    @property
    def http_response(self):
        return self._http_response

    @http_response.setter
    def http_response(self, response: Response):
        self._http_response = response

    @property
    def has_http_response(self):
        return self._http_response is not any_value
