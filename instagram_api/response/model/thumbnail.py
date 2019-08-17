from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['Thumbnail', 'ThumbnailInterface']


class ThumbnailInterface(ApiInterfaceBase):
    video_length: float
    thumbnail_width: int
    thumbnail_height: int
    thumbnail_duration: float
    sprite_urls: [str]
    thumbnails_per_row: int
    max_thumbnails_per_sprite: int
    sprite_width: int
    sprite_height: int
    rendered_width: int


class Thumbnail(PropertyMapper, ThumbnailInterface):
    pass
