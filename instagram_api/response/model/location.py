from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['Location']


class Location(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'name': str,
        'external_id_source': str,
        'external_source': str,
        'address': str,
        'lat': float,
        'lng': float,
        'external_id': str,
        'facebook_places_id': str,
        'city': str,
        'pk': str,
        'short_name': str,
        'facebook_events_id': str,
        'start_time': None,
        'end_time': None,
        'location_dict': 'self',
        'type': None,
        'profile_pic_url': str,
        'profile_pic_username': str,
        'time_granularity': None,
        'timezone': None,
        'country': int,
        'created_at': int,
        'event_category': int,
        'place_fbid': str,
        'place_name': str,
    }
