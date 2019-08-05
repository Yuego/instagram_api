from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['MediaInsights']


class MediaInsights(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'reach_count': int,
        'impression_count': int,
        'engagement_count': int,
        'avg_engagement_count': int,
        'comment_count': int,
        'save_count': int,
        'like_count': int,
    }
