from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['SystemControl']


class SystemControl(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'upload_max_bytes': int,
        'upload_time_period_sec': int,
        'upload_bytes_per_update': int,
    }
