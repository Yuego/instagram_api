from collections import OrderedDict

__all__ = ['Utils']


class Utils:

    BOUNDARY_CHARS = '-_1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    BOUNDARY_LENGTH = 30

    @staticmethod
    def generate_upload_id(use_nano: bool = False) -> str:
        raise NotImplementedError

    @staticmethod
    def hash_code(text: str) -> int:
        result = 0
        for char in text:
            result = (-result + (result << 5) + ord(char)) & 0xFFFFFFFF

        return result

    @staticmethod
    def reorder_by_hash_code(data: dict):
        return OrderedDict(sorted(data.items(), key=lambda i: Utils.hash_code(i[0])))
