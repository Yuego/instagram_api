import pytest

from http.cookiejar import CookieJar
from requests.cookies import RequestsCookieJar

from instagram_api.exceptions import SettingsException
from instagram_api.settings.storage.memory import MemoryStorage


@pytest.fixture()
def empty_storage(request):
    return MemoryStorage()


@pytest.fixture()
def storage(request, jar):
    storage = MemoryStorage()
    storage.cookie_jar_class = RequestsCookieJar

    storage.open({'prefix': ''})
    storage.open_user('test')

    storage.save_user_settings({})
    storage.save_user_cookies(jar)

    return storage


@pytest.fixture()
def jar(request):
    jar = RequestsCookieJar()
    jar.set('c1', 'c1_value', domain='example.com', path='/')
    jar.set('c2', 'c2_value', domain='example.com', path='/')
    return jar


@pytest.fixture()
def empty_jar(request):
    return CookieJar()


@pytest.mark.parametrize(('param', 'expected'), [
    (None, ''),
    ('test', 'test'),
    ('another', 'another'),
])
def test_storage_open(param, expected, empty_storage: MemoryStorage):
    """
    При открытии стораджа только устанавливается префикс
    :param storage:
    :return:
    """
    empty_storage.open({'prefix': param})

    assert empty_storage._prefix == expected


def test_storage_close(storage: MemoryStorage):
    """
    Тест закрытия стораджа
    :param storage:
    :return:
    """
    storage.close()

    assert storage._data == {}


@pytest.mark.parametrize('username', [
    'tester',
    'user',
    'margo',
])
def test_storage_open_close_user(username, empty_storage):
    """
    Тест открытия/закрытия сессии юзера

    :param username:
    :param empty_storage:
    :return:
    """
    assert empty_storage._username is None

    empty_storage.open_user(username)

    assert empty_storage._username == username

    empty_storage.close_user()

    assert empty_storage._username is None


def test_storage_empty_username(empty_storage, empty_jar):
    with pytest.raises(SettingsException):
        empty_storage.load_user_settings()

    with pytest.raises(SettingsException):
        empty_storage.save_user_settings({})

    with pytest.raises(SettingsException):
        empty_storage.load_user_cookies()

    with pytest.raises(SettingsException):
        empty_storage.save_user_cookies(empty_jar)


@pytest.mark.parametrize(('username', 'settings'), [
    ('potato', {'a': 'b'},),
    ('another', {'c': 'd'}),
    ('mark', {'e': 'f'}),
])
def test_data_storing(username, settings, empty_storage, empty_jar):
    empty_storage.open_user(username)

    empty_storage.save_user_cookies(empty_jar)
    empty_storage.save_user_settings(settings)

    cookies = empty_storage.load_user_cookies()
    assert isinstance(cookies, CookieJar)
    assert len(cookies) == 0

    assert empty_storage.load_user_settings() == settings


def test_has_something_methods(storage, empty_jar):

    assert storage.has_user('test') is True
    assert storage.has_user('another') is False

    assert storage.has_user_cookies() is True

    storage.open_user('another')

    assert storage.has_user('another') is False
    assert storage.has_user_cookies() is False

    storage.save_user_settings({})

    assert storage.has_user('another') is True
    assert storage.has_user_cookies() is False

    storage.save_user_cookies(empty_jar)

    assert storage.has_user_cookies() is True
