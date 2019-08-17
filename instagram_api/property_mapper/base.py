import inspect

from instagram_api.interfaces.api_response import ApiResponseInterface

from .exceptions import UnsupportedType, WrongType
from .meta import PropertyMapperMeta, base_allowed_types

__all__ = ['PropertyMapperBase']


class PropertyMapperBase(metaclass=PropertyMapperMeta):

    __attr_dict = {}

    JSON_PROPERTY_MAP = {}

    def parse_json_data(self, data: dict):
        assert isinstance(data, dict), f'{type(data)} is not a `dict`'

        _allowed = ', '.join(map(lambda x: x.__name__, self._allowed_types))
        _cn = self.__class__.__name__

        for data_key, data_value in data.items():

            prop_type = self.JSON_PROPERTY_MAP.get(data_key, None)

            if isinstance(prop_type, (list, tuple)):
                list_prop_type = prop_type[0]

                if isinstance(data_value, (list, tuple)):
                    data_value_list = []
                    for data_item in data_value:
                        data_value_list.append(list_prop_type(data_item))

                    self.__attr_dict[data_key] = data_value_list
                else:
                    raise UnsupportedType(
                        f'`{data_value} isn`t supported for {data_key} attribute of {_cn}.'
                    )
            elif isinstance(prop_type, set):
                for prop_type_variant in prop_type:
                    if issubclass(prop_type_variant, base_allowed_types):
                        if isinstance(data_value, prop_type_variant):
                            self.__attr_dict[data_key] = data_value
                            break
                        else:
                            raise WrongType(
                                f'{data_value} isn`t allowed for attribute {data_key} of {_cn}. '
                                f'Allowed `{prop_type_variant.__name__}`.'
                            )
                    elif issubclass(prop_type_variant, PropertyMapperBase):
                        if isinstance(data_value, dict):
                            self.__attr_dict[data_key] = prop_type_variant(data_value)
                            break
                        else:
                            raise WrongType(
                                f'{data_value} isn`t allowed for attribute {data_key} of {_cn}. Allowed `dict`.'
                            )
                    elif inspect.isfunction(prop_type_variant):
                        self.__attr_dict[data_key] = prop_type_variant(data_value)
                    else:
                        raise UnsupportedType(
                            f'{data_value} isn`t allowed for attribute {data_key} of {_cn}. '
                            f'Allowed are: {_allowed}'
                        )
                else:
                    raise UnsupportedType(
                        f'{data_value} isn`t allowed for attribute {data_key} of {_cn}.'
                        f' Allowed are: {_allowed}'
                    )

            elif prop_type is None:
                self.__attr_dict[data_key] = data_value

            elif inspect.isfunction(prop_type):
                self.__attr_dict[data_key] = prop_type(data_value)

            elif issubclass(prop_type, self._allowed_types):
                if issubclass(prop_type, base_allowed_types):
                    if isinstance(data_value, prop_type):
                        self.__attr_dict[data_key] = data_value
                    else:
                        raise WrongType(
                            f'{data_value} isn`t allowed for attribute {data_key} of {_cn}. '
                            f'Allowed `{prop_type.__name__}`.'
                        )
                elif issubclass(prop_type, PropertyMapperBase):
                    if isinstance(data_value, dict):
                        self.__attr_dict[data_key] = prop_type(data_value)
                    else:
                        raise WrongType(
                            f'{data_value} isn`t allowed for attribute {data_key} of {_cn}. Allowed `dict`.'
                        )
                else:
                    raise UnsupportedType(
                        f'{data_value} isn`t allowed for attribute {data_key} of {_cn}. '
                        f'Allowed are: {_allowed}'
                    )

    def _setattr(self, attr: str, value):
        """
        Internal usage only

        :param attr:
        :param value:
        :return:
        """
        self.__attr_dict[attr] = value

    def _getattr(self, attr: str, default = None):
        if attr in self.__attr_dict:
            return self.__attr_dict[attr]
        elif default:
            return default
        else:
            raise AttributeError(f'{self.__class__.__name__} object has no attribute `{attr}`')

    def __init__(self, data):
        self.parse_json_data(data=data)

    def __setattr__(self, key, value):
        if key in self.__attr_dict:
            raise ValueError('ApiResponse data changing is not allowed')

        super(PropertyMapperBase, self).__setattr__(key, value)

    def __getattr__(self, item):
        if item in self.__attr_dict:
            return self.__attr_dict[item]

        if item in self.JSON_PROPERTY_MAP:
            return None

        return super(PropertyMapperBase, self).__getattribute__(item)
