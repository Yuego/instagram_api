import pytest

from instagram_api.settings.storage.memory import MemoryStorage


@pytest.fixture()
def storage(request):
    return MemoryStorage()


@pytest.mark.parametrize(('param', 'expected'), [
    (None, '_ig'),
    ('test', 'test'),
    ('another', 'another'),
])
def test_storage_open(param, expected, storage: MemoryStorage):
    """
    При открытии стораджа только устанавливается префикс
    :param storage:
    :return:
    """
    storage.open({'prefix': param})

    assert storage._prefix == expected


def test_storage_close(storage: MemoryStorage):
    """
    Должен обнулять данные стораджа
    :param storage:
    :return:
    """

    storage._data = {'a': 'b'}

    storage.close()

    assert storage._data == {}
