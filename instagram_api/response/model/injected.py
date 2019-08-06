from instagram_api.property_mapper import PropertyMapperBase

from .hide_reason import HideReason

__all__ = ['Injected']


class Injected(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'label': str,
        'show_icon': bool,
        'hide_label': str,
        'invalidation': None,
        'is_demo': bool,
        'view_tags': None,
        'is_holdout': bool,
        'tracking_token': str,
        'show_ad_choices': bool,
        'ad_title': str,
        'about_ad_params': str,
        'direct_share': bool,
        'ad_id': int,
        'display_viewability_eligible': bool,
        'fb_page_url': str,
        'hide_reasons_v2': [HideReason],
        'hide_flow_type': int,
        'cookies': [str],
        'lead_gen_form_id': int,
    }
