from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['TraceControl']


class TraceControl(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'max_trace_timeout_ms': int,
    }
