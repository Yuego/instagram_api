
from instagram_api import request
from .experiments_interface import ExperimentsInterface
from .devices.interface import DeviceInterface
from .instagram_base import InstagramInterface


class Instagram(ExperimentsInterface, InstagramInterface):

    EXPERIMENTS_REFRESH = 7200

    username: str
    password: str
    device: DeviceInterface
    debug: bool
    debug_truncate: bool
    debug_developer: bool = False

    uuid: str
    adversiting_id: str
    device_id: str
    phone_id: str
    account_id: int

    is_maybe_logged_in: bool = False

    client: Client

    settings: Settings

    session_id: str

    experiments: list

    account: request.Account
    business: request.Business
    collection: request.Collection
    creative: request.Creative
    direct: request.Direct
    discover: request.Discover
    hashtag: request.Hashtag
    highlight: request.Highlight
    tv: request.TV
    internal: request.Internal
    live: request.Live
    location: request.Location
    media: request.Media
    people: request.People
    push: request.Push
    shopping: request.Shopping
    story: request.Story
    timeline: request.Timeline
    usertag: request.Usertag

    def __init__(self, storage_config: dict, debug: bool = False, debug_truncate: bool = False):
        self.debug = debug
        self.debug_truncate = debug_truncate

        self.account = request.Account(self)
        self.business = request.Business(self)
        self.collection = request.Collection(self)
        self.creative = request.Creative(self)
        self.direct = request.Direct(self)
        self.discover = request.Discover(self)
        self.hashtag = request.Hashtag(self)
        self.highlight = request.Highlight(self)
        self.tv = request.TV(self)
        self.internal = request.Internal(self)
        self.live = request.Live(self)
        self.location = request.Location(self)
        self.media = request.Media(self)
        self.people = request.People(self)
        self.push = request.Push(self)
        self.shopping = request.Shopping(self)
        self.story = request.Story(self)
        self.timeline = request.Timeline(self)
        self.usertag = request.Usertag(self)


