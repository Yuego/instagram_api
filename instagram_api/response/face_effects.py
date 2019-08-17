from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Effect

__all__ = ['FaceEffectsResponse']


class FaceEffectsResponseInterface(ApiResponseInterface):
    sdk_version: AnyType
    effects: [Effect]
    loading_effect: Effect


class FaceEffectsResponse(ApiResponse, FaceEffectsResponseInterface):
    pass
