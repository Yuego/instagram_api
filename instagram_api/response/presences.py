from .mapper import ApiResponse, ApiResponseInterface
from .model.unpredictable import PresenceUnpredictableContainer

__all__ = ['PresencesResponse']


class PresencesResponseInterface(ApiResponseInterface):
    user_presence: PresenceUnpredictableContainer


class PresencesResponse(ApiResponse, PresencesResponseInterface):
    pass
