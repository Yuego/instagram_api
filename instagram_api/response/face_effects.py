from .base_response import Response
from .model import Effect

__all__ = ['FaceEffectsResponse']


class FaceEffectsResponse(Response):
    JSON_PROPERTY_MAP = {
        'sdk_version': None,
        'effects': [Effect],
        'loading_effect': Effect,
    }
