from .mapper import ApiResponse, ApiResponseInterface

from .model import DirectMessageMetadata, Item

__all__ = ['ConfigureResponse']


class ConfigureResponseInterface(ApiResponseInterface):
    upload_id: int
    media: Item
    client_sidecar_id: int
    message_metadata: [DirectMessageMetadata]


class ConfigureResponse(ApiResponse, ConfigureResponseInterface):
    pass
