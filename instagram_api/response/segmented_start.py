from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['SegmentedStartResponse']


class SegmentedStartResponseInterface(ApiResponseInterface):
    stream_id: int


class SegmentedStartResponse(ApiResponse, SegmentedStartResponseInterface):

    def is_ok(self):
        if self.stream_id:
            return True
        else:
            if self.message is None:
                setattr(self, '_message', 'Stream ID for segmented uploader is missing or invalid')

            return False
