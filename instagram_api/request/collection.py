from typing import List

from instagram_api import response

from .base import CollectionBase

__all__ = ['Collection']


class Collection(CollectionBase):

    def get_list(self, max_id: str = None) -> response.GetCollectionsListResponse: ...

    def get_feed(self, collection_id: int, max_id: str = None) -> response.CollectionFeedResponse: ...

    def create(self, name: str, module_name: str = 'collection_create') -> response.CreateCollectionResponse: ...

    def delete(self, collection_id: int) -> response.DeleteCollectionResponse: ...

    def edit(self, collection_id: int, params: dict) -> response.EditCollectionResponse: ...

    def remove_media(self,
                     collection_ids: List[int],
                     media_id: int,
                     module_name: str = 'feed_contextual_saved_collections') -> response.EditCollectionResponse: ...
