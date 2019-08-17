from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['FaceModels', 'FaceModelsInterface']


class FaceModelsInterface(ApiInterfaceBase):
    face_align_model: AnyType
    face_detect_model: AnyType
    pdm_multires: AnyType


class FaceModels(PropertyMapper, FaceModelsInterface):
    pass
