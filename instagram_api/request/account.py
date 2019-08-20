from typing import List

import json
import re

from instagram_api import response
from instagram_api.exceptions import InternalException, SettingsException

from .base import CollectionBase

__all__ = ['Account']


class Account(CollectionBase):

    def get_current_user(self) -> response.UserInfoResponse:
        return self._ig.request('accounts/current_user/').add_params(
            edit=True,
        ).get_response(response.UserInfoResponse)

    def set_biography(self, biography: str) -> response.UserInfoResponse:
        """
         Edit your biography.
     
        You are able to add `@mentions` and `#hashtags` to your biography, but
        be aware that Instagram disallows certain web URLs and shorteners.
     
        Also keep in mind that anyone can read your biography (even if your account is private).

        WARNING: Remember to also call `edit_profile()` after using this
        function, so that you act like the real app!

        :param biography: str
        Biography text. Use "" for nothing.

        :raise: AssertionError

        :return: response.UserInfoResponse
        """
        assert isinstance(biography, str) and len(biography) <= 150, (
            'Please provide a 0 to 150 character string as biography.'
        )

        return self._ig.request('accounts/set_biography/').add_posts(
            raw_text=biography,
            _uuid=self._ig.uuid,
            _uid=self._ig.account_id,
            device_id=self._ig.device_id,
            _csrftoken=self._ig.client.get_token(),
        ).get_response(response.UserInfoResponse)

    def set_gender(self, gender: str = '') -> response.UserInfoResponse:

        g = gender.lower()
        if g == 'male':
            gender_id = 1
        elif g == 'female':
            gender_id = 2
        elif not g:
            gender_id = 3
        else:
            gender_id = 4

        return self._ig.request('accounts/set_gender/').set_signed_post(False).add_posts(
            gender=gender_id,
            _csrftoken=self._ig.client.get_token(),
            _uuid=self._ig.uuid,
            custom_gender=gender if gender_id == 4 else '',
        ).get_response(response.UserInfoResponse)

    def edit_profile(self,
                     url: str,
                     phone: str,
                     name: str,
                     biography: str,
                     email: str,
                     gender: str,
                     new_username: str = None) -> response.UserInfoResponse:
        user_response = self.get_current_user()

        current_user = user_response.user

        if not current_user:
            raise InternalException('Unable to find current account username while preparing profile edit.')

        old_username = current_user.username

        username = new_username if isinstance(new_username, str) and len(new_username) > 0 else old_username

        return self._ig.request('accounts/edit_profile/').add_posts(
            _uuid=self._ig.uuid,
            _uid=self._ig.account_id,
            _csrftoken=self._ig.client.get_token(),
            external_url=url,
            phone_number=phone,
            username=username,
            first_name=name,
            biography=biography,
            email=email,
            gender=gender,
            device_id=self._ig.device_id,
        )

    def change_profile_picture(self, filename: str) -> response.UserInfoResponse:
        ...

    def remove_profile_picture(self) -> response.UserInfoResponse:
        return self._ig.request('accounts/remove_profile_picture/').add_posts(
            _uuid=self._ig.uuid,
            _uid=self._ig.account_id,
            _csrftoken=self._ig.client.get_token(),
        ).get_response(response.UserInfoResponse)

    def set_public(self) -> response.UserInfoResponse:
        return self._ig.request('accounts/set_public/').add_posts(
            _uuid=self._ig.uuid,
            _uid=self._ig.account_id,
            _csrftoken=self._ig.client.get_token(),
        ).get_response(response.UserInfoResponse)

    def set_private(self) -> response.UserInfoResponse:
        return self._ig.request('accounts/set_private/').add_posts(
            _uuid=self._ig.uuid,
            _uid=self._ig.account_id,
            _csrftoken=self._ig.client.get_token(),
        ).get_response(response.UserInfoResponse)

    def switch_to_business_profile(self) -> response.SwitchBusinessProfileResponse:
        return self._ig.request(
            'business_conversion/get_business_convert_social_context/'
        ).get_response(response.SwitchBusinessProfileResponse)

    def switch_to_personal_profile(self) -> response.SwitchPersonalProfileResponse:
        return self._ig.request('accounts/convert_to_personal/').add_posts(
            _uuid=self._ig.uuid,
            _uid=self._ig.account_id,
            _csrftoken=self._ig.client.get_token(),
        ).get_response(response.SwitchPersonalProfileResponse)

    def set_business_info(self,
                          phone_number: str,
                          email: str,
                          category_id: str) -> response.CreateBusinessInfoResponse:
        return self._ig.request('accounts/create_business_info/').add_posts(
            set_public='true',
            entry_point='setting',
            public_phone_contact=json.dumps({
                'public_phone_number': phone_number,
                'business_contact_method': 'CALL',
            }),
            public_email=email,
            category_id=category_id,
            _uuid=self._ig.uuid,
            _uid=self._ig.account_id,
            _csrftoken=self._ig.client.get_token(),
        ).get_response(response.CreateBusinessInfoResponse)

    def check_username(self, username: str) -> response.CheckUsernameResponse:
        return self._ig.request('users/check_username/').add_posts(
            _uuid=self._ig.uuid,
            username=username,
            _csrftoken=self._ig.client.get_token(),
            _uid=self._ig.account_id,
        ).get_response(response.CheckUsernameResponse)

    def get_comment_filter(self) -> response.CommentFilterResponse:
        return self._ig.request('accounts/get_comment_filter/').get_response(response.CommentFilterResponse)

    def set_comment_filter(self, config_value: int) -> response.CommentFilterSetResponse:
        return self._ig.request('accounts/set_comment_filter/').add_posts(
            _uuid=self._ig.uuid,
            _uid=self._ig.account_id,
            _csrftoken=self._ig.client.get_token(),
            config_value=config_value,
        ).get_response(response.CommentFilterSetResponse)

    def get_comment_category_filter_disabled(self) -> response.CommentCategoryFilterResponse:
        return self._ig.request(
            'accounts/get_comment_category_filter_disabled/'
        ).get_response(response.CommentCategoryFilterResponse)

    def get_comment_filter_keywords(self) -> response.CommentFilterKeywordsResponse:
        return self._ig.request(
            'accounts/get_comment_filter_keywords/'
        ).get_response(response.CommentFilterKeywordsResponse)

    def set_comment_filter_keywords(self, keywords: List[str]) -> response.CommentFilterSetResponse:
        return self._ig.request(
            'accounts/set_comment_filter_keywords/'
        ).add_posts(
            _uuid=self._ig.uuid,
            _uid=self._ig.account_id,
            _csrftoken=self._ig.client.get_token(),
            keywords=keywords,
        ).get_response(response.CommentFilterSetResponse)

    def change_password(self, old_password: str, new_password: str) -> response.ChangePasswordResponse:
        return self._ig.request('accounts/change_password/').add_posts(
            _uuid=self._ig.uuid,
            _uid=self._ig.account_id,
            _csrftoken=self._ig.client.get_token(),
            old_password=old_password,
            new_password1=new_password,
            new_password2=new_password,
        ).get_response(response.ChangePasswordResponse)

    def get_security_info(self) -> response.AccountSecurityInfoResponse:
        return self._ig.request('accounts/account_security_info/').add_posts(
            _uuid=self._ig.uuid,
            _uid=self._ig.account_id,
            _csrftoken=self._ig.client.get_token(),
        ).get_response(response.AccountSecurityInfoResponse)

    @staticmethod
    def _clean_phone_number(phone_number: str) -> str:
        return '+' + re.sub(r'[^0-9]', '', phone_number)

    def send_two_factor_enable_sms(self, phone_number: str) -> response.SendTwoFactorEnableSMSResponse:
        cleaned_number = self._clean_phone_number(phone_number)

        return self._ig.request('accounts/send_two_factor_enable_sms/').add_posts(
            _uuid=self._ig.uuid,
            _uid=self._ig.account_id,
            _csrftoken=self._ig.client.get_token(),
            device_id=self._ig.device_id,
            phone_number=cleaned_number,
        ).get_response(response.SendTwoFactorEnableSMSResponse)

    def enable_two_factor_sms(self,
                              phone_number: str,
                              verification_code: str) -> response.EnableTwoFactorSMSResponse:
        cleaned_number = self._clean_phone_number(phone_number)

        return self._ig.request('accounts/enable_sms_two_factor/').add_posts(
            _uuid=self._ig.uuid,
            _uid=self._ig.account_id,
            _csrftoken=self._ig.client.get_token(),
            device_id=self._ig.device_id,
            phone_number=cleaned_number,
            verification_code=verification_code,
        ).get_response(response.EnableTwoFactorSMSResponse)

    def disable_two_factor_sms(self) -> response.DisableTwoFactorSMSResponse:
        return self._ig.request('accounts/disable_sms_two_factor/').add_posts(
            _uuid=self._ig.uuid,
            _uid=self._ig.account_id,
            _csrftoken=self._ig.client.get_token(),
        ).get_response(response.DisableTwoFactorSMSResponse)

    def _save_presence_status(self, disabled: bool):
        try:
            self._ig.settings.set('presence_disabled', '1' if disabled else '0')
        except SettingsException:
            pass

    def get_presence_status(self) -> response.PresenceStatusResponse:
        result = self._ig.request(
            'accounts/get_presence_disabled/'
        ).set_signed_get(True).get_response(response.PresenceStatusResponse)

        self._save_presence_status(result.disabled)

        return result

    def enable_presence(self) -> response.GenericResponse:
        result = self._ig.request('accounts/set_presence_disabled/').add_posts(
            _uuid=self._ig.uuid,
            _uid=self._ig.account_id,
            disabled='0',
            _csrftoken=self._ig.client.get_token(),
        ).get_response(response.GenericResponse)

        self._save_presence_status(False)

        return result

    def disable_presence(self) -> response.GenericResponse:
        result = self._ig.request('accounts/set_presence_disabled/').add_posts(
            _uuid=self._ig.uuid,
            _uid=self._ig.account_id,
            disabled='1',
            _csrftoken=self._ig.client.get_token(),
        ).get_response(response.GenericResponse)

        self._save_presence_status(True)

        return result

    def send_confirm_email(self) -> response.SendConfirmEmailResponse:
        return self._ig.request('accounts/send_confirm_email/').add_posts(
            _uuid=self._ig.uuid,
            _uid=self._ig.account_id,
            _send_source='edit_profile',
            _csrftoken=self._ig.client.get_token(),
        ).get_response(response.SendConfirmEmailResponse)

    def send_sms_code(self, phone_number: str) -> response.SendSMSCodeResponse:
        cleaned_number = self._clean_phone_number(phone_number)

        return self._ig.request('accounts/send_sms_code/').add_posts(
            _uuid=self._ig.uuid,
            _uid=self._ig.account_id,
            _csrftoken=self._ig.client.get_token(),
            phone_number=cleaned_number,
        )

    def verify_sms_code(self, phone_number: str, verification_code: str) -> response.VerifySMSCodeResponse:
        cleaned_number = self._clean_phone_number(phone_number)

        return self._ig.request('accounts/verify_sms_code/').add_posts(
            _uuid=self._ig.uuid,
            _uid=self._ig.account_id,
            phone_number=cleaned_number,
            verification_code=verification_code,
            _csrftoken=self._ig.client.get_token(),
        ).get_response(response.VerifySMSCodeResponse)

    def set_contact_point_prefill(self, usage: str) -> response.GenericResponse:
        return self._ig.request('accounts/contact_point_prefill/').set_needs_auth(False).add_posts(
            phone_id=self._ig.phone_id,
            _csrftoken=self._ig.client.get_token(),
            usage=usage,
        ).get_response(response.GenericResponse)

    def get_badge_notifications(self) -> response.BadgeNotificationsResponse:
        return self._ig.request('notifications/badge/').set_signed_post(False).add_posts(
            _uuid=self._ig.uuid,
            _csrftoken=self._ig.client.get_token(),
            user_ids=self._ig.account_id,
            phone_id=self._ig.phone_id,
        ).get_response(response.BadgeNotificationsResponse)

    def get_process_contact_point_signals(self) -> response.GenericResponse:
        return self._ig.request('accounts/process_contact_point_signals/').add_posts(
            google_tokens='[]',
            phone_id=self._ig.phone_id,
            _uid=self._ig.account_id,
            _uuid=self._ig.uuid,
            device_id=self._ig.device_id,
            _csrftoken=self._ig.client.get_token(),
        ).get_response(response.GenericResponse)
