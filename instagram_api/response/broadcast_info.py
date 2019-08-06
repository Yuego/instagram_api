from .base_response import Response
from .model import Broadcast

__all__ = ['BroadcastInfoResponse']


class BroadcastInfoResponse(Response, Broadcast):
    JSON_PROPERTY_MAP = {

    }
