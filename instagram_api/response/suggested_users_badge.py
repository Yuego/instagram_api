from .base_response import Response

__all__ = ['SuggestedUsersBadgeResponse']


class SuggestedUsersBadgeResponse(Response):
    JSON_PROPERTY_MAP = {
        'should_badge': None,
        'new_suggestion_ids': [int],
    }
