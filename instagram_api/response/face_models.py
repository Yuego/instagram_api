from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import FaceModels

__all__ = ['FaceModelsResponse']


class FaceModelsResponseInterface(ApiResponseInterface):
    face_models: FaceModels


class FaceModelsResponse(ApiResponse, FaceModelsResponseInterface):
    pass
