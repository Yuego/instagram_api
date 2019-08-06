import hashlib
import hmac
import json
import time
import uuid
from urllib.parse import quote

from .constants import Constants
from .utils import Utils


class Signatures:


    @staticmethod
    def generate_signature(data: str):
        return hmac.new(
            Constants.IG_SIG_KEY.encode('utf-8'),
            data.encode('utf-8'),
            hashlib.sha256,
        ).hexdigest()

    @staticmethod
    def generate_signature_for_post(data: str, skip_quote=False):
        if not skip_quote:
            parsed_data = quote(data)
        else:
            parsed_data = data

        return (
            'ig_sig_key_version='
            + Constants.SIG_KEY_VERSION
            + '&signed_body='
            + Signatures.generate_signature(data)
            + '.'
            + parsed_data
        )

    @staticmethod
    def sign_data(data: dict, exclude: list = None):
        exclude = exclude or []

        result = {}
        for item in exclude:
            if item in data:
                result[item] = data.pop(item)

        for key, value in data.items():
            data[key] = str(value)

        data = json.dumps(Utils.reorder_by_hash_code(data))

        result['ig_sig_key_version'] = Constants.SIG_KEY_VERSION
        result['signed_body'] = Signatures.generate_signature(data) + '.' + data

        return Utils.reorder_by_hash_code(result)

    @staticmethod
    def generate_device_id(seed: str = None) -> str:
        if not seed:
            m = hashlib.md5()
            m.update(str(time.time()).encode('utf-8'))
            seed = m.hexdigest()

        volatile_seed = '9876543210'
        m = hashlib.md5()
        m.update(seed.encode('utf-8'), volatile_seed.encode('utf-8'))
        return 'android-' + m.hexdigest()[:16]

    @staticmethod
    def generate_uuid(keep_dashes: bool = True) -> str:
        generated_uuid = str(uuid.uuid4())
        if keep_dashes:
            return generated_uuid
        else:
            return generated_uuid.replace('-', '')

    @staticmethod
    def is_valid_uuid(text: str) -> bool:
        try:
            uuid.UUID(text)
        except ValueError:
            return False
        else:
            return True
