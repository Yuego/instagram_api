from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['Thumbnail']


class Thumbnail(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'video_length': float,
        'thumbnail_width': int,
        'thumbnail_height': int,
        'thumbnail_duration': float,
        'sprite_urls': [str],
        'thumbnails_per_row': int,
        'max_thumbnails_per_sprite': int,
        'sprite_width': int,
        'sprite_height': int,
        'rendered_width': int,
    }
