from typing import Any, Type

from .format import Format
from .v01 import Format as _FormatV01
from .v02 import Format as _FormatV02
from .v02 import model as _model_v02

CurrentFormat = _FormatV02
current_model = _model_v02

FORMAT_TYPES: list[Type[Format]] = [_FormatV01, _FormatV02]
VERSION_FORMAT_TYPES: dict[str, Type[Format]] = {
    format_type.version: format_type for format_type in FORMAT_TYPES
}


def guess_format_version(project_json_data: dict[str, Any]) -> str:
    return project_json_data.get("version", _FormatV01.version)


__all__ = [
    "Format",
    "CurrentFormat",
    "current_model",
    "FORMAT_TYPES",
    "VERSION_FORMAT_TYPES",
    "guess_format_version",
]
