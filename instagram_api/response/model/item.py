from instagram_api.property_mapper import PropertyMapperBase
from instagram_api.property_mapper.types import timestamp

from .ad_metadata import AdMetadata
from .android_links import AndroidLinks
from .attribution import Attribution
from .audio_context import AudioContext
from .caption import Caption
from .carousel_media import CarouselMedia
from .channel import Channel
from .comment import Comment
from .cover_media import CoverMedia
from .explore import Explore
from .gating import Gating
from .hashtag import Hashtag
from .image_versions2 import ImageVersions2
from .injected import Injected
from .ios_links import IOSLinks
from .location import Location
from .media import Media
from .placeholder import Placeholder
from .product_tags import ProductTags
from .reel_mention import ReelMention
from .reel_share import ReelShare
from .stories import Stories
from .story_app_attribution import StoryAppAttribution
from .story_countdowns import StoryCountdowns
from .story_cta import StoryCta
from .story_hashtag import StoryHashtag
from .story_location import StoryLocation
from .story_question_responder_infos import StoryQuestionResponderInfos
from .story_questions import StoryQuestions
from .suggested_users import SuggestedUsers
from .thumbnail import Thumbnail
from .user import User
from .usertag import Usertag
from .video_versions import VideoVersions

__all__ = ['Item']


class Item(PropertyMapperBase):
    PHOTO = 1
    VIDEO = 2
    CAROUSEL = 8
    AUDIO = 11

    JSON_PROPERTY_MAP = {
        'taken_at': timestamp,
        'pk': int,
        'id': int,
        'device_timestamp': timestamp,

        'media_type': int,
        'dynamic_item_id': str,
        'code': str,
        'client_cache_key': str,
        'filter_type': int,
        'product_type': str,
        'nearly_complete_copyright_match': bool,
        'image_versions2': ImageVersions2,
        'original_width': int,
        'original_height': int,
        'caption_position': float,
        'is_reel_media': bool,
        'video_versions': [VideoVersions],
        'has_audio': bool,
        'video_duration': float,
        'user': User,
        'can_see_insights_as_brand': bool,
        'caption': Caption,
        'title': str,
        'caption_is_edited': bool,
        'photo_of_you': bool,
        'fb_user_tags': Usertag,
        'can_viewer_save': bool,
        'has_viewer_saved': bool,
        'organic_tracking_token': str,
        'follow_hashtag_info': Hashtag,
        'expiring_at': str,
        'is_dash_eligible': int,
        'video_dash_manifest': str,
        'number_of_qualities': int,
        'video_codec': str,
        'thumbnails': Thumbnail,
        'can_reshare': bool,
        'can_reply': bool,
        'can_viewer_reshare': bool,
        'visibility': None,
        'attribution': Attribution,

        'view_count': int,
        'viewer_count': int,
        'comment_count': int,
        'can_view_more_preview_comments': bool,
        'has_more_comments': bool,
        'max_num_visible_preview_comments': int,

        'preview_comments': [Comment],

        'comments': [Comment],
        'comments_disabled': None,
        'reel_mentions': [ReelMention],
        'story_cta': [StoryCta],
        'next_max_id': str,
        'carousel_media': [CarouselMedia],
        'carousel_media_type': int,
        'carousel_media_count': int,
        'likers': [User],
        'like_count': int,
        'preview': str,
        'has_liked': bool,
        'explore_context': str,
        'explore_source_token': str,
        'explore_hide_comments': bool,
        'explore': Explore,
        'impression_token': str,
        'usertags': Usertag,
        'media': Media,
        'stories': Stories,
        'top_likers': [str],
        'facepile_top_likers': [User],
        'direct_reply_to_author_enabled': bool,
        'suggested_users': [SuggestedUsers],
        'is_new_suggestion': bool,
        'comment_likes_enabled': bool,
        'location': [Location],
        'lat': float,
        'lng': float,
        'channel': [Channel],
        'gating': [Gating],
        'injected': [Injected],
        'placeholder': [Placeholder],
        'algorithm': str,
        'connection_id': str,
        'social_context': str,
        'icon': None,
        'media_ids': [int],
        'media_id': int,
        'thumbnail_urls': None,
        'large_urls': None,
        'media_infos': None,
        'value': float,
        'collapse_comments': bool,
        'link': str,
        'link_text': str,
        'link_hint_text': str,
        'iTunesItem': None,
        'ad_header_style': int,
        'ad_metadata': [AdMetadata],
        'ad_action': str,
        'ad_link_type': int,
        'dr_ad_type': int,
        'android_links': [AndroidLinks],
        'ios_links': [IOSLinks],
        'force_overlay': bool,
        'hide_nux_text': bool,
        'overlay_text': str,
        'overlay_title': str,
        'overlay_subtitle': str,
        'fb_page_url': str,
        'playback_duration_secs': None,
        'url_expire_at_secs': None,
        'is_sidecar_child': bool,
        'comment_threading_enabled': bool,
        'cover_media': CoverMedia,
        'saved_collection_ids': [int],
        'boosted_status': None,
        'boost_unavailable_reason': None,
        'viewers': [User],
        'viewer_cursor': None,
        'total_viewer_count': int,
        'multi_author_reel_names': None,
        'screenshotter_user_ids': None,
        'reel_share': ReelShare,
        'organic_post_id': str,
        'sponsor_tags': [User],
        'story_poll_voter_infos': None,
        'imported_taken_at': None,
        'lead_gen_form_id': str,
        'ad_id': int,
        'actor_fbid': int,
        'is_ad4ad': None,
        'commenting_disabled_for_viewer': None,
        'is_seen': bool,
        'story_events': None,
        'story_hashtags': [StoryHashtag],
        'story_polls': None,
        'story_feed_media': None,
        'story_sound_on': None,
        'creative_config': None,
        'story_locations': [StoryLocation],
        'story_sliders': None,
        'story_friend_lists': None,
        'story_product_items': None,
        'story_questions': [StoryQuestions],
        'story_question_responder_infos': [StoryQuestionResponderInfos],
        'story_countdowns': [StoryCountdowns],
        'story_music_stickers': None,
        'supports_reel_reactions': bool,
        'show_one_tap_fb_share_tooltip': bool,
        'has_shared_to_fb': bool,
        'main_feed_carousel_starting_media_id': str,
        'main_feed_carousel_has_unseen_cover_media': bool,
        'inventory_source': str,
        'is_eof': bool,
        'top_followers': [str],
        'top_followers_count': int,
        'story_is_saved_to_archive': bool,
        'timezone_offset': int,
        'product_tags': ProductTags,
        'inline_composer_display_condition': str,
        'inline_composer_imp_trigger_time': int,
        'highlight_reel_ids': [int],
        'total_screenshot_count': int,

        'dominant_color': str,
        'story_app_attribution': StoryAppAttribution,
        'audio': AudioContext,
        'follower_count': int,
        'post_count': int,
        'media_cropping_info': None,
    }

    def item_url(self):
        code = getattr(self, 'code', None)
        if code is None:
            return code

        else:
            return f'https://www.instagram.com/p/{code}/'

    def is_ad(self):
        return getattr(self, 'dr_ad_type', None) is not None
