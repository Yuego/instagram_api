from .base_response import Response

__all__ = ['ResumableOffsetResponse']


class ResumableOffsetResponse(Response):
    JSON_PROPERTY_MAP = {
        'offset': int,
    }

    def is_ok(self):
        offset = getattr(self, 'offset', None)

        if offset is not None and offset > 0:
            return True
        else:
            message = getattr(self, 'message', None)
            if message is None:
                self._setattr('message', 'Offset for resumable uploader is missing or invalid.')

            return False
