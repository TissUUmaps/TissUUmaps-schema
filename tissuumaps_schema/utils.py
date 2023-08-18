from typing import Any

from . import v00, v01

SCHEMA_MODULES = [v00, v01]

current_schema_module = v01


def guess_schema_version(model_data: dict[str, Any]) -> str:
    if "expectedCSV" in model_data:  # TODO is this correct?
        return v00.VERSION
    return model_data.get("schemaVersion", v01.VERSION)
