from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['ResumableOffsetResponse']


class ResumableOffsetResponseInterface(ApiResponseInterface):
    offset: int


class ResumableOffsetResponse(ApiResponse, ResumableOffsetResponseInterface):
    def is_ok(self):
        offset = self.offset

        if offset is not None and offset > 0:
            return True
        else:
            message = self.message
            if message is AnyType:
                setattr(self, '_message', 'Offset for resumable uploader is missing or invalid.')

            return False
