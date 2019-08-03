from datetime import datetime

__all__ = ['timestamp']


def timestamp(timestamp: int):
    if timestamp:
        return datetime.utcfromtimestamp(timestamp)
    else:
        return None
