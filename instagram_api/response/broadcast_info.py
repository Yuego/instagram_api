from .base_response import ApiResponse
from .model import Broadcast

__all__ = ['BroadcastInfoResponse']


class BroadcastInfoResponse(ApiResponse, Broadcast):
    JSON_PROPERTY_MAP = {

    }
