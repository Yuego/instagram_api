
from instagram_api.response.user_info import UserInfoResponse

from .collection import Collection


class Account(Collection):

    def get_current_user(self) -> UserInfoResponse:
        raise NotImplementedError

    def set_biography(self, biography: str) -> UserInfoResponse:
        raise NotImplementedError

    def set_gender(self, gender: str = '') -> UserInfoResponse:
        raise NotImplementedError

    def edit_profile(self,
                     url: str,
                     phone: str,
                     name: str,
                     biography: str,
                     email: str,
                     gender: str,
                     new_username: str = None) -> UserInfoResponse:
        raise NotImplementedError

    def change_profile_picture(self, filename: str) -> UserInfoResponse:
        raise NotImplementedError

    def remove_profile_picture(self) -> UserInfoResponse:
        raise NotImplementedError

    def set_public(self) -> UserInfoResponse:
        raise NotImplementedError
