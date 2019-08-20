import json

from instagram_api import response
from instagram_api.constants import Constants

from .base import CollectionBase

__all__ = ['Creative']


class Creative(CollectionBase):

    @staticmethod
    def _check_location(location: dict = None):
        if location is not None:
            if not all([
                'lat' in location,
                'lng' in location,
                'horizontalAccuracy' in location,
            ]):
                raise ValueError('Your location array must contain keys for `lat`, `lng` and `horizontalAccuracy`.')

            location = {
                'lat': location['lat'],
                'lng': location['lng'],
                'horizontalAccuracy': location['horizontalAccuracy'],
            }
        else:
            location = {}

        return location

    def get_sticker_assets(self,
                           sticker_type: str = 'static_stickers',
                           location: dict = None) -> response.StickerAssetsResponse:
        assert sticker_type == 'static_stickers', 'You must provide a valid sticker type.'

        return self._ig.request('creatives/assets/').add_posts(
            type=sticker_type,
            **self._check_location(location),
        )

    def get_face_models(self) -> response.FaceModelsResponse:
        return self._ig.request('creatives/face_models/').add_posts(
            _uuid=self._ig.uuid,
            _uid=self._ig.account_id,
            _csrftoken=self._ig.client.get_token(),
            aml_facetracker_model_version=12,
        ).get_response(response.FaceModelsResponse)

    def get_face_effects(self, location: dict = None) -> response.FaceEffectsResponse:
        return self._ig.request('creatives/face_effects/').add_posts(
            _uuid=self._ig.uuid,
            _uid=self._ig.account_id,
            _csrftoken=self._ig.client.get_token(),
            supported_capabilities_new=json.dumps(Constants.SUPPORTED_CAPABILITIES),
            **self._check_location(location),
        )
