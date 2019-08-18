import pytest
import httpretty

from instagram_api.instagram import Instagram


def test_read_msisdn_header(instagram: Instagram, internal_msisdn_header_success):
    httpretty.enable()

    response = instagram.internal.read_msisdn_header('ig_select_app')

    response2 = instagram.internal.sync_device_features(True)

    httpretty.disable()
    pass
