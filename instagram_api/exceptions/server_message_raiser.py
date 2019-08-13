from typing import Optional

import re

from collections import OrderedDict
from urllib3.response import HTTPResponse

from instagram_api.response.base_response import Response

from .account_disabled import AccountDisabledException
from .bad_request import BadRequestException
from .challenge_required import ChallengeRequiredException
from .checkpoint_required import CheckpointRequiredException
from .consent_required import ConsentRequiredException
from .endpoint import EndpointException
from .feedback_required import FeedbackRequiredException
from .forced_password_reset import ForcedPasswordResetException
from .incorrect_password import IncorrectPasswordException
from .instagram import InstagramException
from .invalid_sms_code import InvalidSmsCodeException
from .invalid_user import InvalidUserException
from .login_required import LoginRequiredException
from .not_found import NotFoundException
from .sentry_block import SentryBlockException

# Получаем класс самым простым из доступных методов
SRE_Pattern = re.compile('test').__class__

__all__ = ['ServerMessageRaiser']


class ServerMessageRaiser:
    EXCEPTION_MAP = OrderedDict([
        #
        # WARNING: We MUST be sure to list these exception messages in an order
        # which guarantees that they will be properly detected without being
        # detected as something else!
        #
        # For example, the "challenge_required" string ALSO exists inside of
        # "checkpoint_challenge_required", so if we check for ChallengeRequired
        # problems above CheckpointRequired, then we would ALWAYS detect
        # checkpoints as "challenge required" since that string exists in both
        # of them.
        #
        # Always list all exceptions in an order that guarantees that they
        # cannot be misdetected as each other! The exceptions with the longest
        # strings, in case of similar strings, MUST be checked/listed EARLIER!
        #
        # So in that example, CheckpointRequired MUST be listed above
        # ChallengeRequired!
        #
        (LoginRequiredException, [
            'login_required'
        ]),
        (CheckpointRequiredException, [
            'checkpoint_required',  # message
            'checkpoint_challenge_required',  # error_type
        ]),
        (ChallengeRequiredException, [
            'challenge_required'
        ]),
        (FeedbackRequiredException, [
            'feedback_required'
        ]),
        (ConsentRequiredException, [
            'consent_required'
        ]),
        (IncorrectPasswordException, [
            # "The password you entered is incorrect".
            re.compile(r'password(.+?)incorrect', re.I | re.U),  # message
            'bad_password',  # error_type
        ]),
        (InvalidSmsCodeException, [
            # "Please check the security code we sent you and try again".
            re.compile(r'check(.+?)security(.+?)code', re.I | re.U),  # message
            'sms_code_validation_code_invalid',  # error_type
        ]),
        (AccountDisabledException, [
            # "Your account has been disabled for violating our terms".
            re.compile(r'account(.+?)disabled(.+?)violating', re.I | re.U),
        ]),
        (SentryBlockException, [
            'sentry_block',
        ]),
        (InvalidUserException, [
            # "The username you entered doesn't appear to belong to an account"
            re.compile(r'username(.+?)doesn\'t(.+?)belong', re.I | re.U),  # message
            'invalid_user',  # error_type
        ]),
        (ForcedPasswordResetException, [
            re.compile(r'reset(.+?)password', re.I | re.U),
        ]),
    ])

    @classmethod
    def auto_raise(cls,
                   prefix_string: Optional[str],
                   server_message: str,
                   server_response: Response = None,
                   http_response: HTTPResponse = None):

        messages = [server_message]
        server_error_type = None

        if isinstance(server_response, Response):
            if server_response.error_type is not None:
                server_error_type = server_response.error_type
                messages.append(server_error_type)

        exception_class = None

        def check_patterns(message, patterns):
            for pattern in patterns:
                if isinstance(pattern, SRE_Pattern):
                    if pattern.search(message):
                        return True
                elif isinstance(pattern, str):
                    if pattern in message:
                        return True
                else:
                    raise ValueError(f'Unknown pattern type: {type(pattern)}, {pattern}')

            return False

        def iter_exceptions(message):
            for exception, patterns in cls.EXCEPTION_MAP.items():
                if check_patterns(message, patterns):
                    return exception

        for msg in messages:
            exception_class = iter_exceptions(msg)
            if exception_class is not None:
                break

        if exception_class is None:
            http_status_code = http_response.status if http_response is not None else None

            if http_status_code == 400:
                exception_class = BadRequestException
            elif http_status_code == 404:
                exception_class = NotFoundException
            else:
                exception_class = EndpointException

        display_message = server_message if server_message else server_error_type

        if display_message is None:
            display_message = 'Request failed.'

        message_text = f'{prefix_string}: {display_message}' if prefix_string else display_message

        message_text = cls.prettify_message(message_text)

        args = [message_text]
        kwargs = {}

        if isinstance(server_response, Response) and issubclass(exception_class, InstagramException):
            kwargs.update({
                'response': server_response,
            })

        raise exception_class(*args, **kwargs)

    @staticmethod
    def prettify_message(message: str):
        last_char = message[-1] if message else ''
        if last_char not in ['', '.', '!', '?']:
            message += '.'

        message = message.capitalize()

        message = message.replace('_', ' ')

        return message
