from .mapper import ApiResponse

from .model.friendship_status import FriendshipStatusInterface

__all__ = ['FriendshipShowResponse']


class FriendshipShowResponseInterface(FriendshipStatusInterface):
    pass


class FriendshipShowResponse(ApiResponse, FriendshipShowResponseInterface):
    pass
