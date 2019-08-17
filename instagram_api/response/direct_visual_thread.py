from .mapper import ApiResponse
from .model.direct_thread import DirectThreadInterface

__all__ = ['DirectVisualThreadResponse']


class DirectVisualThreadResponseInterface(DirectThreadInterface):
    pass


class DirectVisualThreadResponse(ApiResponse, DirectVisualThreadResponseInterface):
    pass
