from .base_response import ApiResponse
from .model import FaceModels

__all__ = ['FaceModelsResponse']


class FaceModelsResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'face_models': FaceModels,
    }
