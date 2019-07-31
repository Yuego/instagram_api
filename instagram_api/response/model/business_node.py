from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['BusinessNode']


class BusinessNode(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'typename': None,
        'followers_count': None,
        'followers_delta_from_last_week': None,
        'posts_count': None,
        'posts_delta_from_last_week': None,
        'last_week_impressions': None,
        'week_over_week_impressions': None,
        'last_week_reach': None,
        'week_over_week_reach': None,
        'last_week_profile_visits': None,
        'week_over_week_profile_visits': None,
        'last_week_website_visits': None,
        'week_over_week_website_visits': None,
        'last_week_call': None,
        'week_over_week_call': None,
        'last_week_text': None,
        'week_over_week_text': None,
        'last_week_email': None,
        'week_over_week_email': None,
        'last_week_get_direction': None,
        'week_over_week_get_direction': None,
        'average_engagement_count': None,
        'last_week_impressions_day_graph': None,
        'last_week_reach_day_graph': None,
        'last_week_profile_visits_day_graph': None,
        'summary_posts': None,
        'state': None,
        'summary_stories': None,
        'followers_unit_state': None,
        'today_hourly_graph': None,
        'gender_graph': None,
        'all_followers_age_graph': None,
        'followers_top_cities_graph': None,
        'summary_promotions': None,
        'top_posts': None,
    }
