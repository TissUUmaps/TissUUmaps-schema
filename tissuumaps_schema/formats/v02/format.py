from ..format import Format as FormatBase
from ..model import Project as ProjectBase
from ..v01.format import Format as PreviousFormat
from ..v01.model import Project as PreviousProject
from .model import Project


class Format(FormatBase[Project]):
    version = "0.2"
    project_type = Project

    def upgrade(self, project: ProjectBase) -> Project:
        if isinstance(project, self.project_type):
            return project
        if not isinstance(project, PreviousProject):
            project = PreviousFormat().upgrade(project)
        upgraded_project = self.project_type()  # TODO
        return upgraded_project
