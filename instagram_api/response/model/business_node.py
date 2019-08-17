from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['BusinessNode', 'BusinessNodeInterface']


class BusinessNodeInterface(ApiInterfaceBase):
    typename: AnyType
    followers_count: AnyType
    followers_delta_from_last_week: AnyType
    posts_count: AnyType
    posts_delta_from_last_week: AnyType
    last_week_impressions: AnyType
    week_over_week_impressions: AnyType
    last_week_reach: AnyType
    week_over_week_reach: AnyType
    last_week_profile_visits: AnyType
    week_over_week_profile_visits: AnyType
    last_week_website_visits: AnyType
    week_over_week_website_visits: AnyType
    last_week_call: AnyType
    week_over_week_call: AnyType
    last_week_text: AnyType
    week_over_week_text: AnyType
    last_week_email: AnyType
    week_over_week_email: AnyType
    last_week_get_direction: AnyType
    week_over_week_get_direction: AnyType
    average_engagement_count: AnyType
    last_week_impressions_day_graph: AnyType
    last_week_reach_day_graph: AnyType
    last_week_profile_visits_day_graph: AnyType
    summary_posts: AnyType
    state: AnyType
    summary_stories: AnyType
    followers_unit_state: AnyType
    today_hourly_graph: AnyType
    gender_graph: AnyType
    all_followers_age_graph: AnyType
    followers_top_cities_graph: AnyType
    summary_promotions: AnyType
    top_posts: AnyType


class BusinessNode(PropertyMapper, BusinessNodeInterface):
    pass
