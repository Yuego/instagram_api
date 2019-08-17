from .mapper import ApiResponse, ApiResponseInterface

from .model import Reel

__all__ = ['CreateHighlightResponse']


class CreateHighlightResponseInterface(ApiResponseInterface):
    reel: Reel


class CreateHighlightResponse(ApiResponse, CreateHighlightResponseInterface):
    pass
