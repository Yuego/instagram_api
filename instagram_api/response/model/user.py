from instagram_api.property_mapper import PropertyMapperBase

from .biography_entities import BiographyEntities
from .chaining_suggestion import ChainingSuggestion
from .image_candidate import ImageCandidate
from .friendship_status import FriendshipStatus
from .link import Link
from .name_tag import Nametag

__all__ = ['User']


class User(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'username': str,
        'has_anonymous_profile_picture': bool,
        'has_highlight_reels': bool,
        'is_favorite': bool,
        'is_favorite_for_stories': bool,
        'is_favorite_for_highlights': bool,
        'is_interest_account': bool,
        'can_be_reported_as_fraud': bool,
        'profile_pic_url': str,
        'profile_pic_id': int,
        'permission': bool,
        'full_name': str,
        'user_id': int,
        'pk': int,
        'id': str,
        'is_verified': bool,
        'is_private': bool,
        'coeff_weight': None,
        'friendship_status': FriendshipStatus,
        'hd_profile_pic_versions': [ImageCandidate],
        'byline': None,
        'search_social_context': None,
        'unseen_count': None,
        'mutual_followers_count': int,
        'follower_count': int,
        'search_subtitle': str,
        'social_context': None,
        'media_count': int,
        'following_count': int,
        'following_tag_count': int,
        'is_business': bool,
        'usertags_count': int,
        'profile_context': None,
        'biography': str,
        'geo_media_count': int,
        'is_unpublished': bool,
        'allow_contacts_sync': None,
        'show_feed_biz_conversion_icon': None,
        'auto_expand_chaining': None,
        'can_boost_post': None,
        'is_profile_action_needed': bool,
        'has_chaining': bool,
        'has_recommend_accounts': bool,
        'chaining_suggestions': [ChainingSuggestion],
        'include_direct_blacklist_status': None,
        'can_see_organic_insights': bool,
        'has_placed_orders': bool,
        'can_convert_to_business': bool,
        'convert_from_pages': None,
        'show_business_conversion_icon': bool,
        'show_conversion_edit_entry': bool,
        'show_insights_terms': bool,
        'can_create_sponsor_tags': None,
        'hd_profile_pic_url_info': ImageCandidate,
        'usertag_review_enabled': None,
        'profile_context_mutual_follow_ids': [str],
        'profile_context_links_with_user_ids': [Link],
        'has_biography_translation': bool,
        'total_igtv_videos': int,
        'total_ar_effects': int,
        'can_link_entities_in_bio': bool,
        'biography_with_entities': BiographyEntities,
        'max_num_linked_entities_in_bio': int,
        'business_contact_method': str,
        'highlight_reshare_disabled': bool,
        # Business category.

        'category': str,
        'direct_messaging': str,
        'page_name': None,
        'fb_page_call_to_action_id': int,
        'is_call_to_action_enabled': bool,
        'account_type': int,
        'public_phone_country_code': str,
        'public_phone_number': str,
        'contact_phone_number': str,
        'latitude': float,
        'longitude': float,
        'address_street': str,
        'zip': str,
        'city_id': int,
        'city_name': str,
        'public_email': str,
        'is_needy': bool,
        'external_url': str,
        'external_lynx_url': str,
        'email': str,
        'country_code': int,
        'birthday': None,
        'national_number': int,
        'gender': int,
        'phone_number': str,
        'needs_email_confirm': None,
        'is_active': bool,
        'block_at': None,
        'aggregate_promote_engagement': None,
        'fbuid': None,
        'page_id': int,
        'can_claim_page': bool,
        'fb_page_call_to_action_ix_app_id': int,
        'fb_page_call_to_action_ix_url': str,
        'can_crosspost_without_fb_token': bool,
        'fb_page_call_to_action_ix_partner': str,
        'shoppable_posts_count': int,
        'show_shoppable_feed': bool,
        'show_account_transparency_details': bool,
    
        'latest_reel_media': int,
        'has_unseen_besties_media': bool,
        'allowed_commenter_type': str,
        'reel_auto_archive': str,
        'is_directapp_installed': bool,
        'besties_count': int,
        'can_be_tagged_as_sponsor': bool,
        'can_follow_hashtag': bool,
        'has_profile_video_feed': bool,
        'is_video_creator': bool,
        'show_besties_badge': bool,
        'screenshotted': bool,
        'nametag': Nametag,
        'school': None,
        'is_bestie': bool,
        'live_subscription_status': str,
    }
