from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .item import Item
from .direct_thread_item_media import DirectThreadItemMedia
from .action_log import ActionLog
from .direct_link import DirectLink
from .direct_reactions import DirectReactions
from .direct_expiring_summary import DirectExpiringSummary
from .reel_share import ReelShare
from .placeholder import Placeholder
from .location import Location
from .live_video_share import LiveVideoShare
from .live_viewer_invite import LiveViewerInvite
from .user import User
from .story_share import StoryShare
from .media_share import MediaShare
from .video_call_event import VideoCallEvent
from .product_share import ProductShare
from .animated_media import AnimatedMedia
from .felix_share import FelixShare
from .voice_media import VoiceMedia

__all__ = ['DirectThreadItem', 'DirectThreadItemInterface']


class DirectThreadItemInterface(ApiInterfaceBase):
    item_id: int
    item_type: AnyType
    text: str
    media_share: Item
    preview_medias: [Item]
    media: DirectThreadItemMedia
    user_id: int
    timestamp: Timestamp
    client_context: str
    hide_in_thread: AnyType
    action_log: ActionLog
    link: DirectLink
    reactions: DirectReactions
    raven_media: Item
    seen_user_ids: [str]
    expiring_media_action_summary: DirectExpiringSummary
    reel_share: ReelShare
    placeholder: Placeholder
    location: Location
    like: AnyType
    live_video_share: LiveVideoShare
    live_viewer_invite: LiveViewerInvite
    profile: User
    story_share: StoryShare
    direct_media_share: MediaShare
    video_call_event: VideoCallEvent
    product_share: ProductShare
    animated_media: AnimatedMedia
    felix_share: FelixShare
    voice_media: VoiceMedia


class DirectThreadItem(PropertyMapper, DirectThreadItemInterface):
    PLACEHOLDER = 'placeholder'
    TEXT = 'text'
    HASHTAG = 'hashtag'
    LOCATION = 'location'
    PROFILE = 'profile'
    MEDIA = 'media'
    MEDIA_SHARE = 'media_share'
    EXPIRING_MEDIA = 'raven_media'
    LIKE = 'like'
    ACTION_LOG = 'action_log'
    REACTION = 'reaction'
    REEL_SHARE = 'reel_share'
    STORY_SHARE = 'story_share'
    LINK = 'link'
    LIVE_VIDEO_SHARE = 'live_video_share'
    LIVE_VIEWER_INVITE = 'live_viewer_invite'
    PRODUCT_SHARE = 'product_share'
    VIDEO_CALL_EVENT = 'video_call_event'
    VOICE_MEDIA = 'voice_media'
