from .base_response import Response
from .model import Insights

__all__ = ['InsightsResponse']


class InsightsResponse(Response):
    JSON_PROPERTY_MAP = {
        'instagram_user': Insights,
    }
