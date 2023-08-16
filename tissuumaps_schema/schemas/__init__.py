from typing import Any

from . import v01, v02

current = v02

SCHEMA_MODULES = [v01, v02]


def guess_schema_version(model_data: dict[str, Any]) -> str:
    return model_data.get("schemaVersion", v01.VERSION)


__all__ = ["current", "guess_schema_version", "SCHEMA_MODULES"]
