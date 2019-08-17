import inspect

from typing import get_type_hints

from .interface_base import ApiInterfaceBase
from .mapper_base import PropertyMapperBase, allowed_types


__all__ = ['PropertyMapperMeta']


def _check_hint_type(class_name, hint_name, hint_type):
    if hint_type is None:
        raise TypeError(f'Property `{hint_name}` of `{class_name}` can not be AnyType.')
    elif inspect.isfunction(hint_type):
        raise TypeError(f'Property `{hint_name}` of `{class_name}. Functions is not supported. '
                        f'Please subclass the PropertyMapperType class.')
    elif isinstance(hint_type, dict):
        raise TypeError(f'Property `{hint_name}` of `{class_name}`. Dictionary type is not supported.'
                        f'Please subclass the ApiInterfaceBase class.')
    # elif isinstance(hint_type, list):
    #    if len(hint_type) != 1:
    #        raise TypeError(
    #            f'Property `{hint_name}` of `{class_name}`. Typelist can contain only one item.'
    #        )
    elif inspect.isclass(hint_type) and not issubclass(hint_type, allowed_types):
        raise TypeError(
            f'Property `{hint_name}` of `{class_name}`. Unsupported type `{hint_type}`. Supported only simple type, '
            f'`PropertyMapperType` or `ApiInterfaceBase` subclass, '
        )


class PropertyMapperMeta(type):

    def __new__(cls, name, bases, attrs):

        attrs_dict = {}

        for base in bases:
            base_name = base.__class__.__name__

            if issubclass(base, ApiInterfaceBase) and not issubclass(base, PropertyMapperBase):
                hints = get_type_hints(base)

                for hint_name, hint_type in hints.items():
                    # hint_name = hint_name.rstrip('_')

                    if not hasattr(base, hint_name):
                        _check_hint_type(base_name, hint_name, hint_type)

                        if inspect.isclass(hint_type) and issubclass(hint_type, allowed_types):
                            attrs_dict[hint_name] = hint_type
                        elif isinstance(hint_type, (list, tuple)):
                            if len(hint_type) != 1:
                                raise TypeError(
                                    f'Property `{hint_name}` of `{base_name}`. Typelist can contain only one item'
                                )

                            list_item_type = hint_type[0]

                            _check_hint_type(base.__class__.__name__, hint_name, list_item_type)

                            if inspect.isclass(list_item_type) and issubclass(list_item_type, allowed_types):
                                attrs_dict[hint_name] = [list_item_type]
                            else:
                                raise TypeError(
                                    f'Property `{hint_name}` of `{base_name}`. Unsupported type `{list_item_type}`'
                                )

                        elif isinstance(hint_type, set):
                            if len(hint_type) <= 1:
                                raise TypeError(
                                    f'Property `{hint_name}` of `{base_name}`. Typeset must contain more than one item.'
                                )

                            for set_item_type in hint_type:
                                _check_hint_type(base_name, hint_name, set_item_type)

                            attrs_dict[hint_name] = hint_type
                        else:
                            raise TypeError(
                                f'Property `{hint_name}` of `{base_name}`. Unsupported type `{hint_type}`'
                            )

            attrs['_attrs_dict'] = attrs_dict

        for attr_name in attrs_dict.keys():
            get_key = f'_get_{attr_name}'

            if get_key in attrs:

                def make_property(key):
                    key = f'_{key}'
                    method_key = get_key

                    def get_property(self):
                        value = getattr(self, key, None)
                        method = getattr(self, method_key)

                        return method(value)

                    return get_property

                attrs[attr_name] = property(make_property(attr_name))

            else:
                for base in bases:
                    if hasattr(base, get_key):
                        break
                else:
                    def make_property(key):
                        key = f'_{key}'

                        def get_property(self):
                            return getattr(self, key, None)

                        return get_property

                    attrs[attr_name] = property(make_property(attr_name))

        new_class = super().__new__(cls, name, bases, attrs)

        return new_class
