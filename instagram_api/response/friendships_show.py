from .mapper import ApiResponse

from .model.friendship_status import FriendshipStatusInterface

__all__ = ['FriendshipsShowResponse']


class FriendshipShowResponseInterface(FriendshipStatusInterface):
    pass


class FriendshipsShowResponse(ApiResponse, FriendshipShowResponseInterface):
    pass
