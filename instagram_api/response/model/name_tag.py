from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['Nametag']


class Nametag(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'mode': int,
        'gradient': int,
        'emoji': str,
        'selfie_sticker': int,
    }
