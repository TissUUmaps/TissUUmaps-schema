from pydantic import Field

from ..base import SchemaBaseModel

VERSION = "0.2"


class SchemaBaseModelV02(SchemaBaseModel):
    schema_version: str = Field(default=VERSION, alias="schemaVersion")
