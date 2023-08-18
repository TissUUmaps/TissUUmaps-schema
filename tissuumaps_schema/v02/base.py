from pydantic import Field

from ..base import RootSchemaBaseModel

VERSION = "0.2"


class RootSchemaBaseModelV02(RootSchemaBaseModel):
    schema_version: str = Field(default=VERSION, alias="schemaVersion")
