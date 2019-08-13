import pytest
import re

from instagram_api.client.client import Client

from instagram_api.exceptions import (
    AccountDisabledException,
    ChallengeRequiredException,
    CheckpointRequiredException,
    ConsentRequiredException,
    FeedbackRequiredException,
    IncorrectPasswordException,
    InvalidSmsCodeException,
    InvalidUserException,
    LoginRequiredException,
    SentryBlockException,
)
from instagram_api.exceptions.server_message_raiser import ServerMessageRaiser

from instagram_api.response.generic import GenericResponse


def make_response(json_string: str) -> GenericResponse:

    return GenericResponse(Client.api_body_decode(json_string=json_string))


def test_login_required_exception():
    with pytest.raises(LoginRequiredException) as excinfo:

        response = make_response('{"message":"login_required", "logout_reason": 2, "status": "fail"}')

        ServerMessageRaiser.auto_raise(None, response.message, response)

    assert excinfo.value.message == 'Login required.'


def test_feedback_required_exception():
    with pytest.raises(FeedbackRequiredException) as excinfo:

        response = make_response(
            '{"message":"feedback_required","spam":true,"feedback_title":"You\u2019re Temporarily Blocked",'
            '"feedback_message":"It looks like you were misusing this feature by going too fast. '
            'You\u2019ve been blocked from using it.\n\nLearn more about blocks in the Help Center. '
            'We restrict certain content and actions to protect our community. Tell us if you think we made a mistake."'
            ',"feedback_url":"WUT","feedback_appeal_label":"Report problem","feedback_ignore_label":"OK",'
            '"feedback_action":"report_problem","status":"fail"}'
        )

        ServerMessageRaiser.auto_raise(None, response.message, response)

    assert excinfo.value.message == 'Feedback required.'


def test_consent_required_exception():
    with pytest.raises(ConsentRequiredException) as excinfo:

        response = make_response(
            '{"message":"consent_required","consent_data":{"headline":"Updates to Our Terms and Data Policy",'
            '"content":"We\'ve updated our Terms and made some changes to our Data Policy. '
            'Please take a moment to review these changes and let us know that you agree to them.\n\n'
            'You need to finish reviewing this information before you can use Instagram.",'
            '"button_text":"Review Now"},"status":"fail"}'
        )

        ServerMessageRaiser.auto_raise(None, response.message, response)

    assert excinfo.value.message == 'Consent required.'


def test_checkpoint_required_exception():
    with pytest.raises(CheckpointRequiredException) as excinfo:

        response = make_response(
            '{"message":"checkpoint_required","checkpoint_url":"WUT","lock":true,"status":"fail",'
            '"error_type":"checkpoint_challenge_required"}'
        )

        ServerMessageRaiser.auto_raise(None, response.message, response)

    assert excinfo.value.message == 'Checkpoint required.'


def test_challenge_required_exception():
    with pytest.raises(ChallengeRequiredException) as excinfo:

        response = make_response(
            '{"message":"challenge_required","challenge":{"url":"https://i.instagram.com/challenge/",'
            '"api_path":"/challenge/","hide_webview_header":false,"lock":true,"logout":false,"native_flow":true},'
            '"status":"fail"}'
        )

        ServerMessageRaiser.auto_raise(None, response.message, response)

    assert excinfo.value.message == 'Challenge required.'


def test_incorrect_password_exception():
    with pytest.raises(IncorrectPasswordException) as excinfo:

        response = make_response(
            '{"message":"The password you entered is incorrect. Please try again.","invalid_credentials":true,'
            '"error_title":"Incorrect password for WUT","buttons":[{"title":"Try Again","action":"dismiss"}],'
            '"status":"fail","error_type":"bad_password"}'
        )

        ServerMessageRaiser.auto_raise(None, response.message, response)

    assert re.search(r'password.*incorrect', excinfo.value.message, re.I)


def test_account_disabled_exception():
    with pytest.raises(AccountDisabledException) as excinfo:

        response = make_response(
            '{"message":"Your account has been disabled for violating our terms. '
            'Learn how you may be able to restore your account."}'
        )

        ServerMessageRaiser.auto_raise(None, response.message, response)

    assert re.search(r'account.*disabled', excinfo.value.message, re.I)


def test_invalid_user_exception():
    with pytest.raises(InvalidUserException) as excinfo:

        response = make_response(
            '{"message":"The username you entered doesn\'t appear to belong to an account. '
            'Please check your username and try again.","invalid_credentials":true,"error_title":"Incorrect Username",'
            '"buttons":[{"title":"Try Again","action":"dismiss"}],"status":"fail","error_type":"invalid_user"}'
        )

        ServerMessageRaiser.auto_raise(None, response.message, response)

    assert re.search(r'check.*username', excinfo.value.message, re.I)


def test_sentry_block_exception():
    with pytest.raises(SentryBlockException) as excinfo:

        response = make_response(
            '{"message":"Sorry, there was a problem with your request.","status":"fail","error_type":"sentry_block"}'
        )

        ServerMessageRaiser.auto_raise(None, response.message, response)

    assert re.search(r'problem.*request', excinfo.value.message, re.I)


def test_invalid_sms_code_exception():
    with pytest.raises(InvalidSmsCodeException) as excinfo:

        response = make_response(
            '{"message":"Please check the security code we sent you and try again.","status":"fail",'
            '"error_type":"sms_code_validation_code_invalid"}'
        )

        ServerMessageRaiser.auto_raise(None, response.message, response)

    assert re.search(r'check.*code', excinfo.value.message, re.I)
