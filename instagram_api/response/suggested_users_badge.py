from .base_response import ApiResponse

__all__ = ['SuggestedUsersBadgeResponse']


class SuggestedUsersBadgeResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'should_badge': None,
        'new_suggestion_ids': [int],
    }
