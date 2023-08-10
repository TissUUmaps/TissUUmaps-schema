from typing import Any, Optional, Type, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T", bound="SchemaBaseModel")


class SchemaBaseModel(BaseModel):
    _PREVIOUS_MODEL_TYPE: Optional[Type["SchemaBaseModel"]] = None
    schema_version: str = Field(alias="schemaVersion")

    @classmethod
    def parse(
        cls: Type[T], model_data: dict[str, Any], strict: Optional[bool] = None
    ) -> T:
        return cls.model_validate(model_data, strict=strict)

    @classmethod
    def upgrade(cls: Type[T], model: "SchemaBaseModel") -> T:
        if isinstance(model, cls):
            return model
        if cls._PREVIOUS_MODEL_TYPE is not None:
            if not isinstance(model, cls._PREVIOUS_MODEL_TYPE):
                model = cls._PREVIOUS_MODEL_TYPE.upgrade(model)
                assert isinstance(model, cls._PREVIOUS_MODEL_TYPE)
            return cls._upgrade_previous_model(model)
        raise NotImplementedError(f"No upgrade path for version {model.schema_version}")

    @classmethod
    def _upgrade_previous_model(cls: Type[T], previous_model: "SchemaBaseModel") -> T:
        raise NotImplementedError()
