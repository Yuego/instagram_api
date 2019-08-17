from .mapper import ApiResponse, ApiResponseInterface

from .model.unpredictable import FriendshipStatusUnpredictableContainer

__all__ = ['FriendshipsShowManyResponse']


class FriendshipsShowManyResponseInterface(ApiResponseInterface):
    friendship_statuses: FriendshipStatusUnpredictableContainer


class FriendshipsShowManyResponse(ApiResponse, FriendshipsShowManyResponseInterface):
    pass
