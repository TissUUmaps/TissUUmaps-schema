from pydantic import BaseModel


class Project(BaseModel):
    version: str
