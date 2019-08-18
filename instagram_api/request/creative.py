from typing import List

from instagram_api import response

from .base import CollectionBase

__all__ = ['Creative']


class Creative(CollectionBase):

    def get_sticker_assets(self,
                           sticker_type: str = 'static_stickers',
                           location: dict = None) -> response.StickerAssetsResponse: ...

    def get_face_models(self) -> response.FaceModelsResponse: ...

    def get_face_effects(self, location: dict = None) -> response.FaceEffectsResponse: ...
