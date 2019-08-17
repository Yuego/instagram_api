from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['MediaInsights', 'MediaInsightsInterface']


class MediaInsightsInterface(ApiInterfaceBase):
    reach_count: int
    impression_count: int
    engagement_count: int
    avg_engagement_count: int
    comment_count: int
    save_count: int
    like_count: int


class MediaInsights(PropertyMapper, MediaInsightsInterface):
    pass
