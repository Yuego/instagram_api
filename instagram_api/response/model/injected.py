from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .hide_reason import HideReason

__all__ = ['Injected', 'InjectedInterface']


class InjectedInterface(ApiInterfaceBase):
    label: str
    show_icon: bool
    hide_label: str
    invalidation: AnyType
    is_demo: bool
    view_tags: AnyType
    is_holdout: bool
    tracking_token: str
    show_ad_choices: bool
    ad_title: str
    about_ad_params: str
    direct_share: bool
    ad_id: int
    display_viewability_eligible: bool
    fb_page_url: str
    hide_reasons_v2: [HideReason]
    hide_flow_type: int
    cookies: [str]
    lead_gen_form_id: int


class Injected(PropertyMapper, InjectedInterface):
    pass
