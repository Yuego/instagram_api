from .base_response import Response

__all__ = ['SegmentedStartResponse']


class SegmentedStartResponse(Response):
    JSON_PROPERTY_MAP = {
        'stream_id': int,
    }

    def is_ok(self):
        stream_id = getattr(self, 'stream_id', None)

        if stream_id:
            return True
        else:
            message = getattr(self, 'message', None)

            if message is None:
                self._setattr('message', 'Stream ID for segmented uploader is missing or invalid')

            return False
