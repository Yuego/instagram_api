
from instagram_api.property_mapper import PropertyMapper

from .model import UnknownMessage


class Response(PropertyMapper):



    JSON_PROPERTY_MAP = {
        '_message': [UnknownMessage],
    }

    @property
    def is_ok(self):
        return getattr(self, 'status') == Response.STATUS_OK
