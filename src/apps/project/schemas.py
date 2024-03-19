from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field

from src.core.domain.settings import DATETIME_FORMAT


class CreateProjectParams(BaseModel):
    name: str = Field(min_length=1, max_length=20)
    desc: str | None = Field(default=None, min_length=1, max_length=200)
    tags: list | None = None


class ProjectBase(BaseModel):
    id: int
    name: str
    desc: str | None = None
    tags: list | None = None
    unique_id: UUID
    created_time: datetime

    class Config:
        json_encoders = {datetime: lambda v: v.strftime(DATETIME_FORMAT)}


class CreateProject(ProjectBase):
    pass


class QueryProjectList(ProjectBase):
    pass
