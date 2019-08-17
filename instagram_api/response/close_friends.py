from .mapper import ApiResponse

from .model.close_friends import CloseFriendsInterface

__all__ = ['CloseFriendsResponse']


class CloseFriendsResponseInterface(CloseFriendsInterface):
    next_max_id: str


class CloseFriendsResponse(ApiResponse, CloseFriendsResponseInterface):
    pass
