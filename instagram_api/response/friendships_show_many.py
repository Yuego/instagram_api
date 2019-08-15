from .base_response import ApiResponse

__all__ = ['FriendshipsShowManyResponse']


class FriendshipsShowManyResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'friendship_statuses': 'Model\UnpredictableKeys\FriendshipStatusUnpredictableContainer',
    }
