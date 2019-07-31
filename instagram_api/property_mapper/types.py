from datetime import datetime

__all__ = ['timestamp']


def timestamp(timestamp: int):
    return datetime.utcfromtimestamp(timestamp)
