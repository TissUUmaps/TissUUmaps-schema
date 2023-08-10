from typing import Type

from tissuumaps_schema.schemas.base import SchemaBaseModel

from ..v01 import Project as PreviousProject
from ._v02 import SchemaBaseModelV02


class Project(SchemaBaseModelV02):
    _PREVIOUS_MODEL_TYPE: Type[SchemaBaseModel] = PreviousProject

    @classmethod
    def _upgrade_previous_model(cls, previous_model: SchemaBaseModel) -> "Project":
        assert isinstance(previous_model, PreviousProject)
        raise NotImplementedError()
