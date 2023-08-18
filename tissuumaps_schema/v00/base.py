from pydantic import Field

from ..base import RootSchemaBaseModel

VERSION = "0.0"


class RootSchemaBaseModelV00(RootSchemaBaseModel):
    schema_version: str = Field(default=VERSION, alias="schemaVersion")
