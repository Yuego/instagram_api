from .base_response import ApiResponse

__all__ = ['GenericResponse']


class GenericResponse(ApiResponse):
    JSON_PROPERTY_MAP = {}
