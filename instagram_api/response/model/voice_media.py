from instagram_api.property_mapper import PropertyMapperBase

from .direct_thread_item_media import DirectThreadItemMedia

__all__ = ['VoiceMedia']


class VoiceMedia(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'media': DirectThreadItemMedia,
    }
