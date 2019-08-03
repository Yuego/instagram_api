from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['FaceModels']


class FaceModels(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'face_align_model': None,
        'face_detect_model': None,
        'pdm_multires': None,
    }
