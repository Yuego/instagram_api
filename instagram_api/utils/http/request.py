from requests import Request as RequestsRequest

from requests.utils import guess_filename, to_key_val_list

from urllib3 import encode_multipart_formdata
from urllib3.fields import RequestField

from instagram_api.utils import Utils

__all__ = ['Request']


class Request(RequestsRequest):

    @staticmethod
    def _encode_files(files: dict, data: dict):
        """Build the body for a multipart/form-data request.

        Will successfully encode files when passed as a dict or a list of
        tuples. Order is retained if data is a list of tuples but arbitrary
        if parameters are supplied as a dict.
        The tuples may be 2-tuples (filename, fileobj), 3-tuples (filename, fileobj, contentype)
        or 4-tuples (filename, fileobj, contentype, custom_headers).
        """
        if not files:
            raise ValueError("Files must be provided.")
        elif isinstance(data, str):
            raise ValueError("Data must not be a string.")

        index = {}
        index.update(data)
        index.update(files)
        index = Utils.reorder_by_hash_code(index)

        new_fields = []

        for key, value in index.items():
            if key in files:
                # support for explicit filename
                ft = None
                fh = None
                if isinstance(value, (tuple, list)):
                    if len(value) == 2:
                        fn, fp = value
                    elif len(value) == 3:
                        fn, fp, ft = value
                    else:
                        fn, fp, ft, fh = value
                else:
                    fn = guess_filename(value) or key
                    fp = value

                if isinstance(fp, (str, bytes, bytearray)):
                    fdata = fp
                elif hasattr(fp, 'read'):
                    fdata = fp.read()
                elif fp is None:
                    continue
                else:
                    fdata = fp

                rf = RequestField(name=key, data=fdata, filename=fn, headers=fh)
                rf.make_multipart(content_type=ft)
                new_fields.append(rf)

            elif key in data:
                if isinstance(value, str) or not hasattr(value, '__iter__'):
                    value = [value]
                for value in value:
                    if value is not None:
                        # Don't call str() on bytestrings: in Py3 it all goes wrong.
                        if not isinstance(value, bytes):
                            value = str(value)

                        new_fields.append(
                            (key.decode('utf-8') if isinstance(key, bytes) else key,
                             value.encode('utf-8') if isinstance(value, str) else value))

        body, content_type = encode_multipart_formdata(new_fields)

        # TODO: compress body

        return body, content_type
