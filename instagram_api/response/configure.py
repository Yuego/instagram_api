from .base_response import ApiResponse
from .model import DirectMessageMetadata, Item

__all__ = ['ConfigureResponse']


class ConfigureResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'upload_id': int,
        'media': Item,
        'client_sidecar_id': int,
        'message_metadata': [DirectMessageMetadata],
    }
