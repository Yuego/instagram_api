
from .base import PropertyMapperBase
from .error_list import PropertyMapperErrorList


class PropertyMapper(PropertyMapperBase):

    STATUS_OK = 'ok'
    STATUS_FAIL = 'fail'

    JSON_PROPERTY_MAP = {
        'status': str,
        'message': {str, PropertyMapperErrorList},
    }

    def __bool__(self):
        return self.status == PropertyMapper.STATUS_OK
