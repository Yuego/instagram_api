from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['AndroidLinks']


class AndroidLinks(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'linkType': 'int',
        'webUri': str,
        'androidClass': str,
        'package': str,
        'deeplinkUri': str,
        'callToActionTitle': str,
        'redirectUri': str,
        'igUserId': str,
        'leadGenFormId': str,
        'canvasDocId': str,
    }
