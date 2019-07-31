__all__ = ['FACEBOOK_OTA_FIELDS']


FACEBOOK_OTA_FIELDS = '%2C'.join([
    'update%7Bdownload_uri',
    'download_uri_delta_base',
    'version_code_delta_base',
    'download_uri_delta',
    'fallback_to_full_update',
    'file_size_delta',
    'version_code',
    'published_date',
    'file_size',
    'ota_bundle_type',
    'resources_checksum%7D'
])
