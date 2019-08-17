from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import (
    AdsInfo,
    FormerUsernameInfo,
    PrimaryCountryInfo,
    SharedFollowerAccountsInfo,
)

__all__ = ['AccountDetailsResponse']


class AccountDetailsResponseInterface(ApiResponseInterface):
    date_joined: str
    former_username_info: FormerUsernameInfo
    primary_country_info: PrimaryCountryInfo
    shared_follower_accounts_info: SharedFollowerAccountsInfo
    ads_info: AdsInfo


class AccountDetailsResponse(ApiResponse, AccountDetailsResponseInterface):
    pass
