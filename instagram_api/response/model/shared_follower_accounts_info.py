from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['SharedFollowerAccountsInfo', 'SharedFollowerAccountsInfoInterface']


class SharedFollowerAccountsInfoInterface(ApiInterfaceBase):
    has_shared_follower_accounts: bool


class SharedFollowerAccountsInfo(PropertyMapper, SharedFollowerAccountsInfoInterface):
    pass
