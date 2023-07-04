from typing import Any, Generic, Optional, Type, TypeVar

from .model import Project

TProject = TypeVar("TProject", bound=Project)


class Format(Generic[TProject]):
    version: str
    project_type: Type[TProject]

    def upgrade(self, project: Project) -> TProject:
        if isinstance(project, self.project_type):
            return project
        raise ValueError(f"Unsupported version: {project.version}")

    def parse(
        self, project_data: dict[str, Any], strict: Optional[bool] = None
    ) -> TProject:
        return self.project_type.model_validate(project_data, strict=strict)
