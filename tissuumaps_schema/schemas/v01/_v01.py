from pydantic import Field

from ..base import SchemaBaseModel

VERSION = "0.1"


class SchemaBaseModelV01(SchemaBaseModel):
    schema_version: str = Field(default=VERSION, alias="schemaVersion")
