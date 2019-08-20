from typing import List

import json

from instagram_api import response

from .base import CollectionBase

__all__ = ['Collection']


class Collection(CollectionBase):

    def get_list(self, max_id: str = None) -> response.GetCollectionsListResponse:
        request = self._ig.request('collections/list/').add_params(
            collection_types=json.dumps([
                'ALL_MEDIA_AUTO_COLLECTION',
                'MEDIA',
                'PRODUCT_AUTO_COLLECTION'
            ])
        )

        if max_id is not None:
            request.add_params(max_id=max_id)

        return request.get_response(response.GetCollectionsListResponse)

    def get_feed(self, collection_id: int, max_id: str = None) -> response.CollectionFeedResponse:
        request = self._ig.request(f'feed/collection/{collection_id}/')

        if max_id is not None:
            request.add_params(max_id=max_id)

        return request.get_response(response.CollectionFeedResponse)

    def create(self, name: str, module_name: str = 'collection_create') -> response.CreateCollectionResponse:
        return self._ig.request('collections/create/').add_posts(
            module_name=module_name,
            collection_visibility='0',
            _csrftoken=self._ig.client.get_token(),
            _uid=self._ig.account_id,
            name=name,
            _uuid=self._ig.uuid,
        ).get_response(response.CreateCollectionResponse)

    def delete(self, collection_id: int) -> response.DeleteCollectionResponse:
        return self._ig.request(f'collections/{collection_id}/delete/').add_posts(
            _uuid=self._ig.uuid,
            _uid=self._ig.account_id,
            _csrftoken=self._ig.client.get_token(),
        ).get_response(response.DeleteCollectionResponse)

    def edit(self, collection_id: int, params: dict) -> response.EditCollectionResponse:

        post_data = {}
        name = params.get('name', None)
        if name:
            post_data['name'] = name

        cover_media_id = params.get('cover_media_id', None)
        if cover_media_id:
            post_data['cover_media_id'] = cover_media_id

        add_media = params.get('add_media', None)
        if add_media and isinstance(add_media, dict):
            post_data['added_media_ids'] = json.dumps(add_media.values())

            module_name = params.get('module_name', 'feed_saved_add_to_collection')
            post_data['module_name'] = module_name

        if not post_data:
            raise ValueError('You must provide a name or at least one media ID.')

        return self._ig.request(f'collections/{collection_id}/edit/').add_posts(
            _uuid=self._ig.uuid,
            _uid=self._ig.account_id,
            _csrftoken=self._ig.client.get_token(),
            **post_data,
        )

    def remove_media(self,
                     collection_ids: List[int],
                     media_id: int,
                     module_name: str = 'feed_contextual_saved_collections') -> response.EditCollectionResponse:
        return self._ig.request(f'media/{media_id}/save/').add_posts(
            module_name=module_name,
            removed_collection_ids=json.dumps(collection_ids),
            radio_type='wifi-none',
            _uuid=self._ig.uuid,
            _uid=self._ig.account_id,
            _csrftoken=self._ig.client.get_token(),
        ).get_response(response.EditCollectionResponse)
