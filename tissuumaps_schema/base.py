from typing import Any, ClassVar, Optional, Type, TypeVar

from pydantic import BaseModel, ConfigDict, Field

from tissuumaps_schema.utils import (
    MAJOR_SCHEMA_VERSION_MODULES,
    get_major_version,
    guess_schema_version,
)


class SchemaBaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


TRoot = TypeVar("TRoot", bound="RootSchemaBaseModel")


class RootSchemaBaseModel(SchemaBaseModel):
    _previous_model_type: ClassVar[Optional[Type["RootSchemaBaseModel"]]] = None
    schema_version: str = Field(alias="schemaVersion")

    @classmethod
    def parse(
        cls: Type[TRoot], model_data: dict[str, Any], strict: Optional[bool] = None
    ) -> TRoot:
        schema_version = guess_schema_version(model_data)
        major_schema_version = get_major_version(schema_version)
        schema_module = MAJOR_SCHEMA_VERSION_MODULES[major_schema_version]
        model_instance = schema_module.model_validate(model_data, strict=strict)
        return cls.upgrade(model_instance)

    @classmethod
    def upgrade(cls: Type[TRoot], old_model_instance: "RootSchemaBaseModel") -> TRoot:
        if isinstance(old_model_instance, cls):
            return old_model_instance
        if cls._previous_model_type is not None:
            if not isinstance(old_model_instance, cls._previous_model_type):
                old_model_instance = cls._previous_model_type.upgrade(
                    old_model_instance
                )
                assert isinstance(old_model_instance, cls._previous_model_type)
            return cls._upgrade_previous(old_model_instance)
        raise NotImplementedError(
            f"No upgrade path for version {old_model_instance.schema_version}"
        )

    @classmethod
    def _upgrade_previous(
        cls: Type[TRoot], previous_model_instance: "RootSchemaBaseModel"
    ) -> TRoot:
        raise NotImplementedError()
