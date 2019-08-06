from .base_response import Response

__all__ = ['LauncherSyncResponse']


class LauncherSyncResponse(Response):
    JSON_PROPERTY_MAP = {
        'configs': None,
    }
