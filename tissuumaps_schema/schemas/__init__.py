from typing import Any

from . import v01, v02
from .base import RootSchemaBaseModel

current = v02

SCHEMA_MODULES = [v01, v02]
SCHEMA_VERSION_MODULES = {
    schema_module.VERSION: schema_module for schema_module in SCHEMA_MODULES
}


def guess_schema_version(model_data: dict[str, Any]) -> str:
    return model_data.get("schemaVersion", v01.VERSION)


__all__ = [
    "current",
    "guess_schema_version",
    "RootSchemaBaseModel",
    "SCHEMA_MODULES",
    "SCHEMA_VERSION_MODULES",
]
