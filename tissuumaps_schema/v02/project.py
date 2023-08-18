from typing import Type

from ..base import RootSchemaBaseModel
from ..v01 import Project as PreviousProject
from .base import RootSchemaBaseModelV02


class Project(RootSchemaBaseModelV02):
    _previous_model_type: Type[RootSchemaBaseModel] = PreviousProject

    @classmethod
    def _upgrade_from_previous_model(
        cls, previous_model: RootSchemaBaseModel
    ) -> "Project":
        assert isinstance(previous_model, PreviousProject)
        raise NotImplementedError()
