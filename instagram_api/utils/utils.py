import re

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

    @staticmethod
    def extract_urls(text: str):
        urls = []

        url_pattern = (
            r'((?:(http|https|Http|Https|rtsp|Rtsp):\/\/'
            r'(?:(?:[a-zA-Z0-9$\-\_\.\+\!\*\'\(\)\,\;\?\&\=]'
            r'|(?:\%[a-fA-F0-9]{2})){1,64}(?:\:(?:[a-zA-Z0-9$\-\_\.\+\!\*\'\(\)\,\;\?\&\=]'
            r'|(?:\%[a-fA-F0-9]{2})){1,25})?\@)?)?'
            r'((?:(?:[a-zA-Z0-9\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF\_]'
            r'[a-zA-Z0-9\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF\_\-]{0,64}\.)+'
            r'(?:(?:aero|arpa|asia|a[cdefgilmnoqrstuwxz])'
            r'|(?:biz|b[abdefghijmnorstvwyz])'
            r'|(?:cat|com|coop|c[acdfghiklmnoruvxyz])'
            r'|d[ejkmoz]|(?:edu|e[cegrstu])|f[ijkmor]|(?:gov|g[abdefghilmnpqrstuwy])|h[kmnrtu]'
            r'|(?:info|int|i[delmnoqrst])|(?:jobs|j[emop])|k[eghimnprwyz]|l[abcikrstuvy]'
            r'|(?:mil|mobi|museum|m[acdeghklmnopqrstuvwxyz])|(?:name|net|n[acefgilopruz])'
            r'|(?:org|om)|(?:pro|p[aefghklmnrstwy])|qa|r[eosuw]|s[abcdeghijklmnortuvyz]'
            r'|(?:tel|travel|t[cdfghjklmnoprtvwz])|u[agksyz]|v[aceginu]|w[fs]'
            r'|(?:\u03B4\u03BF\u03BA\u03B9\u03BC\u03AE'
            r'|\u0438\u0441\u043F\u044B\u0442\u0430\u043D\u0438\u0435|\u0440\u0444'
            r'|\u0441\u0440\u0431|\u05D8\u05E2\u05E1\u05D8'
            r'|\u0622\u0632\u0645\u0627\u06CC\u0634\u06CC'
            r'|\u0625\u062E\u062A\u0628\u0627\u0631|\u0627\u0644\u0627\u0631\u062F\u0646'
            r'|\u0627\u0644\u062C\u0632\u0627\u0626\u0631'
            r'|\u0627\u0644\u0633\u0639\u0648\u062F\u064A\u0629'
            r'|\u0627\u0644\u0645\u063A\u0631\u0628|\u0627\u0645\u0627\u0631\u0627\u062A'
            r'|\u0628\u06BE\u0627\u0631\u062A|\u062A\u0648\u0646\u0633'
            r'|\u0633\u0648\u0631\u064A\u0629|\u0641\u0644\u0633\u0637\u064A\u0646'
            r'|\u0642\u0637\u0631|\u0645\u0635\u0631'
            r'|\u092A\u0930\u0940\u0915\u094D\u0937\u093E|\u092D\u093E\u0930\u0924'
            r'|\u09AD\u09BE\u09B0\u09A4|\u0A2D\u0A3E\u0A30\u0A24'
            r'|\u0AAD\u0ABE\u0AB0\u0AA4|\u0B87\u0BA8\u0BCD\u0BA4\u0BBF\u0BAF\u0BBE'
            r'|\u0B87\u0BB2\u0B99\u0BCD\u0B95\u0BC8'
            r'|\u0B9A\u0BBF\u0B99\u0BCD\u0B95\u0BAA\u0BCD\u0BAA\u0BC2\u0BB0\u0BCD'
            r'|\u0BAA\u0BB0\u0BBF\u0B9F\u0BCD\u0B9A\u0BC8|\u0C2D\u0C3E\u0C30\u0C24\u0C4D'
            r'|\u0DBD\u0D82\u0D9A\u0DCF|\u0E44\u0E17\u0E22|\u30C6\u30B9\u30C8'
            r'|\u4E2D\u56FD|\u4E2D\u570B|\u53F0\u6E7E|\u53F0\u7063|\u65B0\u52A0\u5761'
            r'|\u6D4B\u8BD5|\u6E2C\u8A66|\u9999\u6E2F|\uD14C\uC2A4\uD2B8|\uD55C\uAD6D'
            r'|xn\-\-0zwm56d|xn\-\-11b5bs3a9aj6g|xn\-\-3e0b707e|xn\-\-45brj9c|xn\-\-80akhbyknj4f|xn\-\-90a3ac'
            r'|xn\-\-9t4b11yi5a|xn\-\-clchc0ea0b2g2a9gcd|xn\-\-deba0ad|xn\-\-fiqs8s|xn\-\-fiqz9s|xn\-\-fpcrj9c3d'
            r'|xn\-\-fzc2c9e2c|xn\-\-g6w251d|xn\-\-gecrj9c|xn\-\-h2brj9c|xn\-\-hgbk6aj7f53bba|xn\-\-hlcj6aya9esc7a'
            r'|xn\-\-j6w193g|xn\-\-jxalpdlp|xn\-\-kgbechtv|xn\-\-kprw13d|xn\-\-kpry57d|xn\-\-lgbbat1ad8j'
            r'|xn\-\-mgbaam7a8h|xn\-\-mgbayh7gpa|xn\-\-mgbbh1a71e|xn\-\-mgbc0a9azcg|xn\-\-mgberp4a5d4ar'
            r'|xn\-\-o3cw4h|xn\-\-ogbpf8fl|xn\-\-p1ai|xn\-\-pgbs0dh|xn\-\-s9brj9c|xn\-\-wgbh1c|xn\-\-wgbl6a'
            r'|xn\-\-xkc2al3hye2a|xn\-\-xkc2dl3a5ee0h|xn\-\-yfro4i67o|xn\-\-ygbi2ammx|xn\-\-zckzah|xxx)'
            r'|y[et]|z[amw]))|(?:(?:25[0-5]|2[0-4][0-9]|[0-1][0-9]{2}|[1-9][0-9]|[1-9])\.'
            r'(?:25[0-5]|2[0-4][0-9]|[0-1][0-9]{2}|[1-9][0-9]|[1-9]|0)\.(?:25[0-5]|2[0-4][0-9]|[0-1][0-9]{2}|[1-9][0-9]'
            r'|[1-9]|0)\.(?:25[0-5]|2[0-4][0-9]|[0-1][0-9]{2}|[1-9][0-9]|[0-9])))(?:\:\d{1,5})?)'
            r'(\/(?:(?:[a-zA-Z0-9\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF'
            r'\;\/\?\:\@\&\=\#\~\-\.\+\!\*\'\(\)\,\_])|(?:\%[a-fA-F0-9]{2}))*)?(?:\b|$)'
        )

        re_links = re.compile(url_pattern)

        for match in re_links.finditer(text):
            urls.append({
                'full_url': match[0],
                'base_url': match[1],
                'protocol': match[2],
                'domain': match[3],
                'path': match[4],
            })

        return urls
