from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['AudioContext']


class AudioContext(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'audio_src': str,
        'duration': int,
    }
