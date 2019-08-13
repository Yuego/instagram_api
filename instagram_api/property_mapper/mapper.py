from urllib3.response import HTTPResponse


from .base import PropertyMapperBase
from .error_list import PropertyMapperErrorList


class PropertyMapper(PropertyMapperBase):

    STATUS_OK = 'ok'
    STATUS_FAIL = 'fail'

    JSON_PROPERTY_MAP = {
        'status': str,
        'message': {str, PropertyMapperErrorList},
        'error_type': str,
    }

    _http_response: HTTPResponse

    def __bool__(self):
        return self.status == PropertyMapper.STATUS_OK

    @property
    def is_ok(self):
        return self.status == self.STATUS_OK

    @property
    def get_message(self):
        message = self._getattr('message', None)

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
    def http_response(self, response: HTTPResponse):
        self._http_response = response

    @property
    def has_http_response(self):
        return self._http_response is not None
