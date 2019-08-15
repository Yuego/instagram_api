from .base_response import ApiResponse

__all__ = ['LauncherSyncResponse']


class LauncherSyncResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'configs': None,
    }
