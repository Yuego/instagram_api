from instagram_api.property_mapper import PropertyMapperBase

from .product import Product
from .user import User

__all__ = ['In']


class In(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'position': [float],
        'user': User,
        'time_in_video': None,
        'start_time_in_video_in_sec': None,
        'duration_in_video_in_sec': None,
        'product': Product,
    }
