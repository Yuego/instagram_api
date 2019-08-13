import pytest

from instagram_api.devices.device import Device
from instagram_api.devices.good import GoodDevices


@pytest.fixture()
def device_default_kwargs(request):
    return dict(
        app_version='1',
        version_code='1',
        user_locale='ru_RU',
        auto_fallback=False
    )


def test_device_initialisation(device_default_kwargs):
    with pytest.raises(AssertionError) as excinfo:

        kwargs = dict(
            device_string='',
        )
        kwargs.update(device_default_kwargs)

        Device(**kwargs)

    assert excinfo.value.args[0] == 'Device string is empty'

    with pytest.raises(AssertionError) as excinfo:

        kwargs = dict(
            device_string='24/7.0; 380dpi; OnePlus; ONEPLUS A3010; OnePlus3T; qcom'
        )
        kwargs.update(device_default_kwargs)

        Device(**kwargs)

    assert 'not conform' in excinfo.value.args[0]

    with pytest.raises(AssertionError) as excinfo:

        kwargs = dict(
            device_string='24/2.1; 380dpi; 1080x1920; OnePlus; ONEPLUS A3010; OnePlus3T; qcom'
        )
        kwargs.update(device_default_kwargs)

        Device(**kwargs)

    assert 'required Android' in excinfo.value.args[0]

    with pytest.raises(AssertionError) as excinfo:

        kwargs = dict(
            device_string='24/7.0; 380dpi; 1080x1900; OnePlus; ONEPLUS A3010; OnePlus3T; qcom'
        )
        kwargs.update(device_default_kwargs)

        Device(**kwargs)

    assert 'resolution' in excinfo.value.args[0]


@pytest.mark.parametrize('device_string', GoodDevices.DEVICES)
def test_device_string_parsing(device_string, device_default_kwargs):
    kwargs = dict(
        device_string=device_string,
    )
    kwargs.update(device_default_kwargs)
    dev = Device(**kwargs)

    result_device_string = '; '.join([
        '/'.join([dev.android_version, dev.android_release]),
        dev.dpi,
        dev.resolution,
        '/'.join([dev.manufacturer, dev.brand]) if dev.brand else dev.manufacturer,
        dev.model,
        dev.device,
        dev.cpu,
    ])

    assert device_string == result_device_string
