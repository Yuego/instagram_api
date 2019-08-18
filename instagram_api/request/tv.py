from instagram_api import response

from .base import CollectionBase

__all__ = ['Tv']


class Tv(CollectionBase):

    def get_tv_guide(self) -> response.TvGuideResponse: ...

    def get_channel(self, id: str = 'for_you', max_id: str = None) -> response.TvChannelsResponse: ...

    def upload_video(self, video_filename: str, external_metadata: dict = None) -> response.ConfigureResponse: ...

    def search(self, query: str = '') -> response.TvSearchResponse: ...

    def write_seen_state(self,
                         impression: str,
                         view_progress: int = 0,
                         grid_impressions: list = None) -> response.GenericResponse: ...
