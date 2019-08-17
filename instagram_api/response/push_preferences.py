from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import PushSettings

__all__ = ['PushPreferencesResponse']


class PushPreferencesResponseInterface(ApiResponseInterface):
    push_settings: [PushSettings]
    likes: AnyType
    comments: AnyType
    comment_likes: AnyType
    like_and_comment_on_photo_user_tagged: AnyType
    live_broadcast: AnyType
    new_follower: AnyType
    follow_request_accepted: AnyType
    contact_joined: AnyType
    pending_direct_share: AnyType
    direct_share_activity: AnyType
    user_tagged: AnyType
    notification_reminders: AnyType
    first_post: AnyType
    announcements: AnyType
    ads: AnyType
    view_count: AnyType
    report_updated: AnyType


class PushPreferencesResponse(ApiResponse, PushPreferencesResponseInterface):
    pass
