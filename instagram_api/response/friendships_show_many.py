from .base_response import Response

__all__ = ['FriendshipsShowManyResponse']


class FriendshipsShowManyResponse(Response):
    JSON_PROPERTY_MAP = {
        'friendship_statuses': 'Model\UnpredictableKeys\FriendshipStatusUnpredictableContainer',
    }
