from instagram_api import response

from .base import CollectionBase

__all__ = ['Business']


class Business(CollectionBase):

    def get_insights(self, day: int = None) -> response.InsightsResponse: ...

    def get_media_insights(self, media_id: int) -> response.MediaInsightsResponse: ...

    def get_statistics(self) -> response.GraphQLResponse: ...
