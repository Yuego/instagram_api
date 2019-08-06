from .base_response import Response
from .model import FaceModels

__all__ = ['FaceModelsResponse']


class FaceModelsResponse(Response):
    JSON_PROPERTY_MAP = {
        'face_models': FaceModels,
    }
