from .base_response import ApiResponse
from .model import Effect

__all__ = ['FaceEffectsResponse']


class FaceEffectsResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'sdk_version': None,
        'effects': [Effect],
        'loading_effect': Effect,
    }
