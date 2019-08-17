from .mapper import ApiResponse

from .model.hashtag import HashtagInterface

__all__ = ['TagInfoResponse']


class TagInfoResponseInterface(HashtagInterface):
    pass


class TagInfoResponse(ApiResponse, TagInfoResponseInterface):
    pass
