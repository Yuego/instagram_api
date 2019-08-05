from instagram_api.property_mapper import PropertyMapperBase

from .broadcast import Broadcast

__all__ = ['LiveViewerInvite']


class LiveViewerInvite(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'text': str,
        'broadcast': Broadcast,
        'title': str,
        'message': str,
    }
