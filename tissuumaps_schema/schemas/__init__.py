from typing import Any

from . import v01, v02
from .base import SchemaBaseModel

current = v02

ALL_SCHEMA_MODULES = [v01, v02]
SCHEMA_MODULES_BY_VERSION = {
    schema_module.VERSION: schema_module for schema_module in ALL_SCHEMA_MODULES
}


def guess_schema_version(model_data: dict[str, Any]) -> str:
    return model_data.get("schemaVersion", v01.VERSION)


__all__ = [
    "current",
    "SchemaBaseModel",
    "ALL_SCHEMA_MODULES",
    "SCHEMA_MODULES_BY_VERSION",
    "guess_schema_version",
]
