from ..format import Format as FormatBase
from .model import Project


class Format(FormatBase[Project]):
    version = "0.1"
    project_type = Project
