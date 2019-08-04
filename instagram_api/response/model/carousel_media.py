from instagram_api.property_mapper import PropertyMapperBase

from .ad_metadata import AdMetadata
from .android_links import AndroidLinks
from .headline import Headline
from .image_versions2 import ImageVersions2
from .usertag import Usertag
from .video_versions import VideoVersions

__all__ = ['CarouselMedia']


class CarouselMedia(PropertyMapperBase):
    PHOTO = 1
    VIDEO = 2

    JSON_PROPERTY_MAP = {
        'pk': int,
        'id': int,
        'carousel_parent_id': int,
        'fb_user_tags': Usertag,
        'number_of_qualities': int,
        'is_dash_eligible': int,
        'video_dash_manifest': str,
        'image_versions2': ImageVersions2,
        'video_versions': [VideoVersions],
        'has_audio': bool,
        'video_duration': float,
        'video_subtitles_uri': str,
        'original_height': int,
        'original_width': int,

        'media_type': int,
        'dynamic_item_id': str,
        'usertags': Usertag,
        'preview': str,
        'headline': Headline,
        'link': str,
        'link_text': str,
        'link_hint_text': str,
        'android_links': [AndroidLinks],
        'ad_metadata': [AdMetadata],
        'ad_action': str,
        'ad_link_type': int,
        'force_overlay': bool,
        'hide_nux_text': bool,
        'overlay_text': str,
        'overlay_title': str,
        'overlay_subtitle': str,

        'dominant_color': str,
    }
