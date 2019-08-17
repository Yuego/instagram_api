from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import DirectRankedRecipient

__all__ = ['DirectRankedRecipientsResponse']


class DirectRankedRecipientsResponseInterface(ApiResponseInterface):
    expires: AnyType
    ranked_recipients: [DirectRankedRecipient]
    filtered: AnyType
    request_id: str
    rank_token: str


class DirectRankedRecipientsResponse(ApiResponse, DirectRankedRecipientsResponseInterface):
    pass
