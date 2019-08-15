from .base_response import ApiResponse


class EnableDisableLiveCommentsResponse(ApiResponse):

    JSON_PROPERTY_MAP = {
        'comment_muted': int,
    }
