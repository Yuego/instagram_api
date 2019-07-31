import inspect

from .types import *

__all__ = ['PropertyMapperMeta', 'base_allowed_types']

base_allowed_types = (
    bool,
    int,
    str,
    float,
)

map_attr_name = 'JSON_PROPERTY_MAP'


class PropertyMapperMeta(type):

    def __new__(cls, name, bases, attrs):

        property_types = base_allowed_types

        cls_property_map = attrs.get(map_attr_name, None)

        if cls_property_map is None:
            raise ValueError(f'Please define {map_attr_name} attribute of {name}')

        elif not isinstance(cls_property_map, dict):
            raise ValueError(f'{map_attr_name} attribute of {name} must be a `dict` type')

        base_property_map = {}
        for base in bases:
            if base.__name__ == 'PropertyMapperBase':
                property_types += (base,)

            base_property_map.update(getattr(base, map_attr_name, {}))

        property_map = base_property_map
        property_map.update(cls_property_map)

        attrs[map_attr_name] = property_map
        attrs['_allowed_types'] = property_types

        for prop_name, prop_type in property_map.items():

            if isinstance(prop_type, dict):
                raise ValueError(f'Property: {prop_name} of {name}. `dict` type isn`t supported')
            elif isinstance(prop_type, (list, tuple)):
                if len(prop_type) != 1:
                    raise ValueError(f'Property: {prop_name} of {name}. Typelist can contain only one item')

                else:
                    list_item_type = prop_type[0]
                    if (
                        not issubclass(list_item_type, property_types)
                        and not isinstance(list_item_type, cls)
                        and not inspect.isfunction(list_item_type)
                    ):
                        raise ValueError(
                            f'Property: {prop_name} of {name}.'
                            f' Typelist can contain only simple type, function '
                            f'or another PropertyMapperBase object'
                        )
            elif isinstance(prop_type, set):
                if len(prop_type) <= 1:
                    raise ValueError(
                        f'Property: {prop_name} of {name}. '
                        f'Typeset must contain more than 1 item'
                    )

                for set_item_type in prop_type:
                    if (
                        not issubclass(set_item_type, property_types)
                        and not isinstance(set_item_type, cls)
                        and not inspect.isfunction(set_item_type)
                    ):
                        raise ValueError(
                            f'Property: {prop_name} of {name}.'
                            f' Typeset can contain only simple types, functions '
                            f'or another PropertyMapperBase objects'
                        )
            elif inspect.isfunction(prop_type):
                pass

            elif prop_type is None:
                pass

            elif not inspect.isclass(prop_type):
                raise ValueError(
                    f'Property: {prop_name} of {name} must be class, not an instance!'
                )

            elif not issubclass(prop_type, property_types) and not isinstance(prop_type, cls):
                raise ValueError(
                    f'Property: {prop_name}. Only simple types supported and subclasses of PropertyMapperBase'
                )

        return super().__new__(cls, name, bases, attrs)
