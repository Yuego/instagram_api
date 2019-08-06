from .base_response import Response


class EnableDisableLiveCommentsResponse(Response):

    JSON_PROPERTY_MAP = {
        'comment_muted': int,
    }
